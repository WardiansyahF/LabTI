#include <iostream>
#include <queue>
#include <stack>
#include <vector>

using namespace std;

class Graf {
private:
    int vertices;
    vector<vector<int> > adjacencyList;

public:
    Graf(int v) : vertices(v), adjacencyList(v + 1) {}

    void tambahSisi(int v, int w) {
        adjacencyList[v].push_back(w);
        adjacencyList[w].push_back(v); // If the graph is undirected, add this line.
    }

    void BFS(int mulai) {
    vector<bool> dikunjungi(vertices + 1, false);
    queue<int> q;
    q.push(mulai);
    dikunjungi[mulai] = true;

    while (!q.empty()) {
        int saatIni = q.front();
        cout << saatIni << " ";
        q.pop();

        // Reverse the order of neighbors
        for (vector<int>::iterator it = adjacencyList[saatIni].begin(); it != adjacencyList[saatIni].end(); ++it) {
            int tetangga = *it;
            if (!dikunjungi[tetangga]) {
                q.push(tetangga);
                dikunjungi[tetangga] = true;
            }
        }
    }
}

void DFS(int mulai) {
    vector<bool> dikunjungi(vertices + 1, false);
    stack<int> s;
    s.push(mulai);

    while (!s.empty()) {
        int saatIni = s.top();
        s.pop();

        if (!dikunjungi[saatIni]) {
            cout << saatIni << " ";
            dikunjungi[saatIni] = true;
        }

        // Reverse the order of neighbors
        for (vector<int>::reverse_iterator it = adjacencyList[saatIni].rbegin(); it != adjacencyList[saatIni].rend(); ++it) {
            int tetangga = *it;
            if (!dikunjungi[tetangga]) {
                s.push(tetangga);
            }
        }
    }
}
};

int main() {
    int vertices, edges;
    cout << "Masukkan jumlah simpul: ";
    cin >> vertices;
    Graf graf(vertices);

    cout << "Masukkan jumlah sisi: ";
    cin >> edges;

    cout << "Masukkan sisi-sisi (format: sumber tujuan):" << endl;
    for (int i = 0; i < edges; ++i) {
        int sumber, tujuan;
        cin >> sumber >> tujuan;
        graf.tambahSisi(sumber, tujuan);
    }

    int pilihan;
    do {
        cout << "\nMenu:\n1. Breadth-First Search (BFS)\n2. Depth-First Search (DFS)\n0. Keluar\nMasukkan pilihan: ";
        cin >> pilihan;

        switch (pilihan) {
            case 1:
                cout << "Masukkan simpul awal untuk BFS: ";
                int bfsMulai;
                cin >> bfsMulai;
                cout << "Hasil traversal BFS: ";
                graf.BFS(bfsMulai);
                cout << endl;
                break;

            case 2:
                cout << "Masukkan simpul awal untuk DFS: ";
                int dfsMulai;
                cin >> dfsMulai;
                cout << "Hasil traversal DFS: ";
                graf.DFS(dfsMulai);
                cout << endl;
                break;

            case 0:
                cout << "Keluar dari program. Selamat tinggal!\n";
                break;

            default:
                cout << "Pilihan tidak valid. Harap masukkan opsi yang benar.\n";
        }
    } while (pilihan != 0);

    return 0;
}