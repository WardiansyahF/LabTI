#include <stdio.h>
#include <stdlib.h>

int q[20], top = -1, front = -1, rear = -1, a[20][20], vis[20], stack[20];

void add(int item);
int del();
int pop();
void push(int item);

void bfs(int s, int n);
void dfs(int s, int n);

void add(int item){
  if(rear == 19){
    printf("Antrian Full");
  }else{
    if(rear == -1){
      q[++rear] = item;
      front++;
    }else{
      q[++rear] = item;
    }
  }
}

int del(){
  int k;

  if((front > rear) || (front == -1)){
    return 0;
  }else{
    k = q[front++];
    return k;
  }
}

void push(int item){
  if(top == 10){
    printf("Stack Overflow");
  }else{
    stack[++top] = item;
  }
}

int pop(){
  int k;

  if(top == -1){
    return 0;
  }else{
    k = stack[top--];
    return k;
  }
}

void bfs(int s, int n){
  int p, i;
  add(s);
  vis[s] = 1;
  p = del();

  if (p != 0){
    printf("%d", p);
  }
  
  while(p != 0){
    for (i = 1; i <= n; i++){
      if((a[p][i] != 0) && (vis[i] == 0)){
        add(i);
        vis[i] = 1;
      }
      p = del();
      if (p != 0){
        printf("%d", p);
      }
    }
  }

  for (i = 1; i <= n; i++){
    if (vis[i] == 0){
      bfs(i,n);
    }
  }
}

void dfs(int s, int n){
  int i, k;

  push(s);

  vis[s] = 1;
  k = pop();

  if(k != 0){
    printf("%d", k);
  }

  while(k != 0){
    for(i = 1; i <= n; i++){
      if((a[k][i] != 0) && (vis[i] == 0)){
        push(i);
        vis[i] = 1;
      }
      k = pop();
      if(k != 0){
        printf("%d", k);
      }
    }
    for (i = 1; i <= n; i++){
      if(vis[i] == 0){
        dfs(i,n);
      }
    }
  }
}




int main(){
  int n, i, s, ch, j;
  char c;
  printf("Masukkan Angka : ");
  scanf("%d", &n);

  for (i = 1; i <= n; i++){
    for (j = 1; j <= n; j++){
      printf("Masukkan 1 jika %d terhubung dengan %d selain itu masukkan 0 : ", i, j);
      scanf("%d", &a[i][j]);
    }
  }

  printf("\n Matriks Adjensi\n");
  for(i = 1; i <= n; i++){
    for(j = 1; j <=n; j++){
      printf("%d", a[i][j]);
    }
    printf("\n");
  }

  do{
    for (i = 1; i <= n; i++)
      a: vis[i] = 0;
    printf("\nMenu");
    printf("\n1. BFS");
    printf("\n2. DFS");
    printf("\nPilihan : ");
    scanf("%d", &ch);
    printf("\nMasukkan simpul sumber: ");
    scanf("%d", &s);

    switch(ch){
      case 1: bfs(s,n);
      break;
      case 2: dfs(s,n);
      break;
    }
    printf("\n");
    printf("Apakah Ingin Melanjutkan? (Y/N)");
    scanf(" %c", &c);
    
  }while((c == 'Y') || (c == 'y'));
}


