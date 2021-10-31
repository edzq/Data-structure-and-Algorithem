#include <bits/stdc++.h>

using namespace std;
int merge_sort_counter = 0, insert_sort_counter = 0;
void merge(vector<int> &list, int p, int mid, int q) {
    vector<int> tempList;
    int i = p, j = mid + 1;
    while (i <= mid && j <= q) {
        ++merge_sort_counter;
        if (list[i] <= list[j]) {
            ++merge_sort_counter;
            tempList.push_back(list[i++]);
            ++merge_sort_counter;
        } else {
            ++merge_sort_counter;
            tempList.push_back(list[j++]);
            ++merge_sort_counter;
        }
    }
    while (i <= mid) {
        ++merge_sort_counter;
        tempList.push_back(list[i++]);
        ++merge_sort_counter;
    }
    while (j <= q) {
        ++merge_sort_counter;
        tempList.push_back(list[j++]);
        ++merge_sort_counter;
    }
    int k = 0;
    for (i = p; i <= q; i++) {
        ++merge_sort_counter;
        list[i] = tempList[k++];
        ++merge_sort_counter;
    }

}

void merge_sort(vector<int> &list, int p, int q) {
    if (p < q) {
        //++merge_sort_counter; //new
        int mid = (p + q) / 2;
        merge_sort(list, p, mid);
        merge_sort(list, mid + 1, q);
        merge(list, p, mid, q);
    }
}

void insert_sort(vector<int> &list) {
    int i, j, tmp;
    for (i = 0; i < list.size(); i++) {
        ++insert_sort_counter;
        tmp = list[i];
        j = i - 1;
        ++insert_sort_counter;
        while (j >= 0 && tmp < list[j]) {
            ++insert_sort_counter;
            list[j + 1] = list[j];
            ++insert_sort_counter;
            j--;
        }
        list[j + 1] = tmp;
        ++insert_sort_counter;
    }
}

vector<int> generate_random_list(int n, int l, int r) {
    vector<int> list;
    srand(time(0));
    for (int i = 0; i < n; i++) {
        int x = rand() % (r - l + 1) + l;
        list.push_back(x);
    }
    return list;
}

void test(int list_length, long &total_merge_sort_time, long &total_insert_sort_time, long &total_merge_sort_counter, long &total_insert_sort_counter){
    merge_sort_counter = insert_sort_counter = 0;
    vector<int> list1 = generate_random_list(list_length,0,100);
    vector<int> list2 = list1;
    vector<int> list_origin = list1;

    clock_t start,end;
    double merge_sort_time, insert_sort_time;

    start = clock();
    merge_sort(list1, 0, list1.size() - 1);
    end = clock();
    merge_sort_time = end - start;
    start = clock();
    insert_sort(list2);
    end = clock();
    insert_sort_time = end - start;

    total_insert_sort_counter += insert_sort_counter;
    total_insert_sort_time += insert_sort_time;
    total_merge_sort_counter += merge_sort_counter;
    total_merge_sort_time += merge_sort_time;
    
    cout << "Output: " <<endl;
    cout << "Random generate array: " <<endl;
    for(auto it = list_origin.begin(); it != list_origin.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;
    
    cout << "Insertion sorted array: " <<endl;
    
    for(auto it = list1.begin(); it != list1.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;
    
      cout << "Merge sorted array:  " <<endl;
    
    for(auto it = list2.begin(); it != list2.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;
    
    //cout << "\nlist Size: " << list2.size() << endl;
    //cout << "merge_sort_time: " << merge_sort_time << " ms \ninsert_sort_time:  " << insert_sort_time << " ms" << endl;
    //cout << "merge_sort_counter: " << merge_sort_counter << "\ninsert_sort_counter:  " << insert_sort_counter << "\n" << endl;
}
int main() {
    //int testing_cases_num = 10, list_length = 50000;
    int list_length;
    int testing_cases_num = 1;
    cout<<"Please input the length of array:"<<endl;
	cin >> list_length;
    
    long ave_merge_sort_time = 0, ave_insert_sort_time = 0, ave_merge_sort_counter = 0, ave_insert_sort_counter = 0;
    for(int i = 0; i < testing_cases_num; ++i){
        test(list_length,ave_merge_sort_time,ave_insert_sort_time,ave_merge_sort_counter,ave_insert_sort_counter);
    }
    ave_insert_sort_counter/=testing_cases_num;
    ave_merge_sort_counter/=testing_cases_num;
    ave_insert_sort_time/=testing_cases_num;
    ave_merge_sort_time/=testing_cases_num;
    cout << "total test_cases_num: " << testing_cases_num << endl;
    cout << "every_list_length: " << list_length << "\n" << endl;
    cout << "ave_merge_sort_time: " << ave_merge_sort_time << " ms" << endl;
    cout << "ave_merge_sort_counter: " << ave_merge_sort_counter << endl;
    cout << "ave_insert_sort_time: " << ave_insert_sort_time << " ms" << endl;
    cout << "ave_insert_sort_counter: " << ave_insert_sort_counter << endl;
    return 0;
}