# A Seiva · Cena 1 · Linha aberta (roteiro de áudio v4)

Ideia nova: a cena deixa de ser um **briefing** e vira uma **emergência**. A Lis não está explicando a missão
numa sala; ela está queimando tudo, fugindo, e usando os últimos minutos de rádio. A informação sai aos
pedaços, entre um susto e outro. Voz limpa; efeitos com o sound design. Nenhum pedido ao ouvinte, só o
"Mantenha o ritmo" do livro.

## O que mudou da v3 para a v4

| v3 | v4 |
|---|---|
| Briefing rápido, em ordem lógica | Emergência: ela está fazendo outra coisa enquanto fala (alarme, fogo, gerador) |
| Alívio de uma linha ao conectar | A conexão é **mostrada**: bipes, voz do sistema ("Canal seguro estabelecido"), ela desaba num "Conectou!" |
| Só fala com o corredor | Fala também **consigo mesma** ("Calma, Lis. Foco."): dá pressa e humanidade sem pedir nada a ninguém |
| Descreve a seiva (fungos, pulso, beleza) | Isso sai da cena 1. A poesia da seiva volta no momento calmo depois dos drones, como já está no livro |
| Termina no plano | Termina com um gancho: "Quase." e o pontinho na tela |

Duração: ~1 min 40 s. Cortes naturais para música: depois de T04 e depois de T08.

## Roteiro

**[SOM]** Alarme baixo e distante, algo queimando, ventilação, estática, bipes de busca de canal.

### Bloco 1 · Linha aberta

**T01** *(sussurro tenso, ofegante, colada no microfone)* — pausa 0,4 s, **[SOM]** bipes de busca
> Tá, tá, tá... vai. Conecta. Conecta, por favor.

**T02** *(a voz sobe de uma vez)* — pausa 0,3 s, **[SOM]** bipe de confirmação
> Na escuta? Na escuta?! Aqui é a Lis!

**SISTEMA** *(neutra, automática)* — pausa 0,2 s
> Canal seguro estabelecido.

**T03** *(o ar sai de uma vez, depois ela se recompõe)* — pausa 0,3 s
> Ai, meu Deus. Conectou. Conectou! ... Tá. Calma, Lis. Foco.

**T04** *(já operando, rápida)* — pausa 1,0 s, **[SOM]** passos do corredor entram
> Eu tô te ouvindo. Esses passos... você já tá correndo. Ótimo. Então escuta, porque eu só vou falar uma vez.

### Bloco 2 · O que você carrega

**T05** *(direta)* — pausa 0,4 s
> Aí na sua mochila tem um frasco. Pequeno. Parece nada. E é a única coisa no mundo que eles querem.

**T06** *(rápida, sem respirar)* — pausa 0,4 s
> Dentro dele tá a seiva. Dez anos de trabalho. Energia limpa, de graça, pra todo mundo. Era pra salvar tudo.

**T07** *(a voz cai)* — pausa 0,5 s, **[SOM]** drone grave
> Mas a Vanguarda do Norte descobriu que dá pra virar arma. Uma arma que apaga a vida. De continentes inteiros.

**T08** *(seca)* — pausa 1,0 s, **[SOM]** fogo distante
> Por isso eu queimei o laboratório. Tudo. Dez anos numa noite. Esse frasco é tudo que sobrou.

### Bloco 3 · Por que você, e pra onde

**T09** *(rápida, quase falando sozinha)* — pausa 0,5 s, **[SOM]** floresta, ping de sonar
> E sim, eu sei que você deve estar pensando: por que eu? Eles caçam por calor e por barulho. Barcos, drones, sonar. E você, sozinho, debaixo das árvores? Pra máquina, você é quase nada. Quase. Foi por isso que eu te escolhi.

**T10** *(operadora)* — pausa 0,5 s, **[SOM]** rio ao longe
> Eu tô te vendo aqui na tela. Um pontinho se mexendo no meio do mato. Do outro lado do rio tem um ponto de extração. É pra lá que esse pontinho vai, e eu vou te avisando de cada passo.

**T11** *(promessa)* — pausa 0,6 s
> Nós somos os guardiões agora.

**T12** *(seca)* — **[SOM]** pulso volta, batida de corrida
> Mantenha o ritmo.

## Notas de produção

- **Ritmo sem acelerar a voz:** velocidade perto de 1,0 e **corte seco** nas pausas internas (`apertar_pausas.py`),
  em vez de acelerar. Acelerar muito deixa a fala artificial e não cria pressa de verdade.
- **Voz do sistema:** Supertonic-3 (voz neutra), que serve bem para voz automática. O livro já tem essa voz.
- **O que inventei:** o autodiálogo "Calma, Lis. Foco."; o sistema avisando a conexão já na cena 1; "pontinho na
  tela"; "Foi por isso que eu te escolhi". Dá para cortar qualquer um.
