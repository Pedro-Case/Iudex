#include <bits/stdc++.h>

using namespace std;
struct Objeto
{
    string nome;
    Objeto * prox;
};

int hash_funct(string nome, int tamanho){
    int soma = 0;
    for(int c; nome[c]; c++){
        soma = soma + (int(nome[c])*c);
    }
    soma = (soma * 17) % tamanho;
    return soma;
}

int main(int argc, char *argv[]) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int tamanho, n_nomes, n_entradas;
    string entrada, argumento;
    cin >> tamanho, n_nomes;
    string tabela[tamanho];
    for(int i = 0; i++; i < n_nomes){
        cin >> entrada, argumento;
        Objeto pessoa;
        pessoa.nome = entrada;
        tabela[hash_funct(pessoa.nome, tamanho)];
    }
    cin >> n_entradas;
    for(int i = 0; i++; i < n_entradas){
        cin >> entrada, argumento;
    }
    return 0;
}
