# A Seiva · Cap. 1 · Abertura da Dra. Lis (roteiro de áudio v1)

Voz: perfil **Dra. Lis (Corrigida)** (`079904a9`), idioma `pt`.
Duração estimada de fala: ~75 s, mais ~3,6 s de pausas entre os trechos.

## Direção

A Dra. Lis não lê um relatório. Ela está escondida, com pouco tempo, falando baixo num rádio
que pode cair a qualquer momento. Por isso:

- **Entra no meio da ação.** Primeiro o contato e o alívio ("Graças a Deus"). A apresentação
  vem depois, como confissão, não como ficha técnica.
- **Contraste emocional.** A seiva é descrita com carinho (pulsa como um coração) antes de a
  ameaça aparecer. A queda de tom na virada é o que dá peso à arma biológica.
- **Cada dado termina num comando para o corpo de quem corre.** Sonar e calor viram "fique
  frio, sem deixar o coração disparar". A história passa a pedir algo do ritmo real do
  corredor, que é o que faz o Zombies, Run! funcionar.
- **Frases curtas, reticências e perguntas.** Cada "..." vira uma micropausa na síntese.
  Quem fala sob pressão não faz período composto.

### O que mudei no texto original

| Original | Agora | Por quê |
|---|---|---|
| "Na Escuta? Na escuta?" | "Na escuta? ... Na escuta?" | Pausa de quem espera resposta no rádio |
| "Dra. Lis" | "Doutora Lis" | O TTS pode ler "Dra." soletrado |
| "Já sintetizei a seiva" | "E eu consegui. Eu sintetizei a seiva." | Dá um respiro de orgulho antes do dado |
| "se instabilizada, a seiva cria..." | "Se a seiva for instabilizada... ela vira outra coisa." | Sujeito explícito; soa falado |
| "o consórcio ... internacional" | "o consórcio da Vanguarda do Norte" | "Internacional" não acrescenta nada ouvindo |
| "veículos aquáticos e drones emitiriam calor e ruído no sonar deles" | "Barcos, drones... tudo que eles têm emite calor e barulho. O sonar deles pega tudo." | Quebrado em três ideias curtas |
| "camuflada ... é invisível para as máquinas se mantiver a temperatura baixa" | "Pra máquina, isso é invisível. Desde que você se mantenha frio. Sem pânico." | Vira instrução direta ao corredor |

Nada da trama foi alterado. Os fatos são os mesmos: dez anos de pesquisa, seiva como energia
limpa por mais de dez anos, arma capaz de varrer continentes, laboratório queimado, matriz
original na mochila, extração do outro lado do rio, "guardiões" e "mantenha o ritmo".

## Trechos

| # | Texto enviado à voz | Voz | Pausa depois |
|---|---|---|---|
| 1 · Contato | Na escuta? ... Na escuta? ... Aqui é a Doutora Lis. ... Graças a Deus. O seu sinal conectou. | velocidade 1.0, ofegante, aliviada | 0,9 s |
| 2 · A seiva | Escuta... eu passei os últimos dez anos aqui, no coração dessa floresta. Estudando uma rede de fungos que brilham no escuro. ... E eu consegui. Eu sintetizei a seiva. ... É a coisa mais bonita que eu já vi. Ela pulsa. Como um coração vivo. ... Energia limpa. Por mais de dez anos. | 0.95, mais lenta, quase maravilhada | 0,7 s |
| 3 · A virada | Só que o consórcio da Vanguarda do Norte descobriu uma coisa. ... Se a seiva for instabilizada... ela vira outra coisa. Uma arma biológica. ... Capaz de varrer a vida de continentes inteiros. | 0.90, grave, devagar | 0,6 s |
| 4 · O frasco | Por isso eu queimei o laboratório. ... Tudo. Mas o frasco com a matriz original... está aí. Na sua mochila. ... Isso mesmo. Agora é você quem carrega ele. | 1.05, tensa, mais rápida | 0,5 s |
| 5 · Por que você | Você deve estar se perguntando por que eu escolhi você. ... Barcos, drones... tudo que eles têm emite calor e barulho. O sonar deles pega tudo. ... Mas uma pessoa correndo, escondida debaixo da copa das árvores? ... Pra máquina, isso é invisível. Desde que você se mantenha frio. Sem pânico. Sem deixar o coração disparar. Entendeu? | 1.0, firme, didática mas baixa | 0,9 s |
| 6 · Guardiões | O ponto de extração fica do outro lado do rio. ... Você chega lá. ... Agora, nós somos os guardiões. ... Então corre. E mantenha o ritmo. | 0.95, decidida; "corre" seco | fim |

## Camada de som (para mixar por cima da voz)

- **0:00**: estática de rádio, clique de conexão e a estática cai quando ela fala. Passos
  compassados e respiração baixa de fundo, constantes, na cadência da corrida.
- **Trecho 2**: música sobe um pouco, mais luminosa. Pulso grave suave de ~1 batida por
  segundo, o "coração" da seiva.
- **Trecho 3**: o pulso para. Drone grave e dissonante, música recua.
- **Trecho 4**: crepitar de fogo distante sob a voz (o laboratório queimando).
- **Trecho 5**: floresta, algum ping de sonar muito discreto.
- **Trecho 6**: rio ao longe. Em "mantenha o ritmo" o pulso volta e a batida da música de
  corrida entra, para o corredor sentir que a missão começou.
- **Efeito de rádio na voz**: filtro passa-banda (~300 Hz a 3,3 kHz), leve saturação e
  chiado baixo. Já existe um script que faz isso e junta os trechos: `_tools/assemble.py`.

## Ideias para o app (estilo Zombies, Run!)

- Em vez de um bloco de 75 s, tocar cada trecho como uma "cena" curta entre faixas da música
  do próprio corredor. Fala longa em corrida cansa e se perde no vento e no fone.
- Deixar "mantenha o ritmo" como frase de retorno que a Dra. Lis (e depois o Leo) repete em
  momentos de queda de pace. Cria vínculo com o corpo e dá motivo para ouvir de novo.
- O contraste com o Leo (nervoso, engraçado, estagiário) já está no capítulo. Vale gravar as
  falas dele com outra voz de perfil bem distinta (mais jovem, mais rápida) para o ouvido
  trocar de personagem sem precisar de narração.
