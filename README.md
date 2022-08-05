# Target-Job_Test_Analyst_Júnior

## Repositório destinado ao processo seletivo da empresa Target Sistemas

Instruções gerais
Olá! Estamos muito felizes com a sua participação em nosso processo seletivo :)
Você chegou na fase de teste, o intuito é analisar seus conhecimentos técnicos.
Espero te ver na próxima fase em? Boa sorte! :)

Olá! Bem-vindes ao teste de Analista de Teste :)

Esta prova tem 4 questões e tem o objetivo de compreender um pouco mais dos seus
conhecimentos técnicos,

Separe um tempinho, vá para um ambiente mais calmo e arrase!

Boa sorte!

Certifique-se de reservar tempo suficiente para fazer o teste sem interrupções.
Caso você saia do teste sem finalizá-lo, será considerado como concluído e você
não poderá fazer novamente.

- [x] 1º Pergunta
- [x] 2º Pergunta
- [x] 3º Pergunta
- [x] 4º Pergunta

#### Perguntas:

1) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora de todos os
 dias de um ano, faça um programa, na linguagem que desejar, que calcule e retorne:

- O menor valor de faturamento ocorrido em um dia do ano;
- O maior valor de faturamento ocorrido em um dia do ano;
- Número de dias no ano em que o valor de faturamento diário foi superior à média anual.

*IMPORTANTE*:

Considerar o vetor já carregado com as informações de valor de faturamento.
Podem existir dias sem faturamento, como nos finais de semana e feriados.
Estes dias devem ser ignorados no cálculo da média.
Utilize o algoritmo mais veloz que puder definir.

2) Relacione os seguintes conceitos à sua respectiva descrição.

IMPORTANTE: note que apenas 4 dos 6 conceitos listados possuem uma descrição correspondente.

Conceitos

I – Caso de Uso

II – Coesão

III – Composição

IV – Classe

V – Polimorfismo

VI – Acoplamento


Descrição

A) É um tipo de agregação.

B) É uma medida do grau de dependência entre objetos.

C) É a propriedade por meio da qual um atributo ou variável pode apontar para objetos de diferentes classes em horas diferentes.

D) É comumente definida(o) por suposições, pré-condições, pós-condições, garantias mínimas e garantias de sucesso

R: (III - A) / (VI - C) / (V - D) / (i - B)

3) Banco de dados

Uma empresa solicitou a você um aplicativo para manutenção de um cadastro de clientes. Após a reunião de definição dos requisitos,
as conclusões foram as seguintes:

- Um cliente pode ter um número ilimitado de telefones;

- Cada telefone de cliente tem um tipo, por exemplo: comercial, residencial, celular, etc. O sistema deve permitir 
cadastrar novos tipos de telefone;

- A princípio, é necessário saber apenas em qual estado brasileiro cada cliente se encontra. O sistema deve permitir 
cadastrar novos estados;


Você ficou responsável pela parte da estrutura de banco de dados que será usada pelo aplicativo. Assim sendo:

a) Proponha um modelo lógico para o banco de dados que vai atender a aplicação. Desenhe as tabelas necessárias, 
os campos de cada uma e marque com setas os relacionamentos existentes entre as tabelas;

b) Aponte os campos que são chave primária (PK) e chave estrangeira (FK);

c) Faça uma busca utilizando comando SQL que traga o código, a razão social e o(s) telefone(s) de todos os 
clientes do estado de São Paulo (código “SP”);

Respostas:

https://drive.google.com/file/d/1KQhKLKCigibiH5_-sLWY6_FPPskxwFun/view?usp=sharing

SELECT c.id as codigo, c.razaoSocial, t.tipo, t.ddd, t.numero
FROM Clientes as c, Telefones as t, Estados as e
WHERE c.id = t.idCliente and e.id = c.idEstado and regiao = 'SP'

4) Observe o trecho de código abaixo:
```c
int INDICE = 13, SOMA = 0, K = 0;
enquanto K < INDICE faça
{
  K = K + 1;
  SOMA = SOMA + K;
}
imprimir(SOMA);
```
Ao final do processamento, qual será o valor da variável SOMA?

Resposta: 91