# Referências de emoção da Dra. Lis (para gravar com a sua voz e converter pelo RVC)

Cada gravação vira **uma referência** de um perfil no VoiceStudio. A emoção da referência é a emoção que a voz
sintética vai copiar, então **atue de verdade**: o resultado imita o seu jeito de falar.

## Como gravar
- **Onde:** quarto silencioso, sem eco, sem ventilador, sem música. Cobertores ou roupas por perto ajudam.
- **Microfone:** a um palmo da boca, sempre à mesma distância e no mesmo lugar, nas 5 gravações.
- **Formato:** WAV, mono, 44,1 ou 48 kHz. Sem redução de ruído, sem compressor, sem efeito.
- **Volume:** forte o bastante para não ficar baixo, sem estourar. Evite picos no máximo.
- **Duração:** de **10 a 20 s** cada. O VoiceStudio usa no máximo 20 s de referência.
- **Como ler:** não leia como texto. Fale como a Lis falaria, com pausas e respirações reais. Se errar uma
  palavra, mantenha o ritmo e siga, desde que o sentido fique.
- **Onde salvar:** `D:\voz_conversao\gravacoes\` com os nomes abaixo (`lis_tensa.wav` etc.).
- **Uma ou duas tentativas por emoção.** Se uma ficar melhor, fique com ela.

Importante: o tom da sua voz não precisa ser agudo. O script calcula sozinho quantos semitons subir.

## Prioridade
Comece pelas **3 primeiras**. As outras vêm depois, se a conversão e os perfis funcionarem.

### 1. `lis_tensa.wav` — urgente, ofegante, baixa e rápida
*Direção: ela está escondida e com pressa, olhando por cima do ombro. A voz treme um pouco. Alívio no
"conectou", urgência logo depois.*
> Tá, tá, tá, vai. Conecta, por favor. Na escuta? Na escuta?! Aqui é a Lis! Ai, meu Deus, conectou. Calma, Lis, foco. Eu tô te ouvindo, você já tá correndo, ótimo. Escuta, eu só vou falar uma vez.

Usa nas falas: T01 a T04 da cena 1.

### 2. `lis_firme.wav` — operadora, controlada, objetiva
*Direção: ela já se recompôs. Voz clara, firme, de quem dá instruções e acompanha o corredor numa tela.*
> Eu tô te vendo aqui na tela, um pontinho se mexendo no meio do mato. Do outro lado do rio tem um ponto de extração. É pra lá que esse ponto vai, e eu vou te avisando de cada passo. Daqui pra frente somos só eu e você.

Usa nas falas: T05, T06, T10 e T11.

### 3. `lis_grave.wav` — sombria, séria, mais lenta
*Direção: a voz cai. É o peso da notícia. Devagar, sem dramatizar demais, com pausas.*
> A Vanguarda do Norte descobriu a seiva, e eles não querem energia limpa. Se ela for instabilizada, vira uma arma que apaga a vida. Continentes inteiros. Eu fiz as contas três vezes. Torci pra errar nas três.

Usa nas falas: T07, T08 e T09.

### 4. `lis_baixa.wav` — voz baixa, quase sussurrada (opcional)
*Direção: ela se esconde de alguém. Fale baixo, perto do microfone, mas **com voz**, não sussurro sem som.*
> Fica em silêncio. Tem alguém no corredor. Eu consigo ouvir os passos, estão chegando perto. Não faz barulho. Eu vou desligar o rádio por um minuto, e quando for seguro, eu volto.

**Atenção:** o RVC depende do tom da voz. Um sussurro verdadeiro, sem vibração das cordas vocais, costuma
converter mal. Por isso peço voz baixa, não sussurro puro.

### 5. `lis_panico.wav` — assustada, a voz sobe e quebra (opcional)
*Direção: ela percebe que foi encontrada. Respiração curta, frases cortadas. Cuidado para não estourar o
volume nos gritos: afaste um pouco o microfone.*
> Espera, não, não, não! Como eles me acharam? Eles estão no meu bunker! Eu vou destruir o terminal, não deixa eles verem as suas coordenadas! Não toquem em mim!

Usa na cena do bunker invadido.

### 6. `lis_encantada.wav` — emocionada, maravilhada (opcional)
*Direção: a Lis cientista que ama a seiva. Calor, um sorriso na voz, ritmo mais solto.*
> Você precisava ver. Ela pulsa, de verdade, como um coração vivo. Eu fiquei horas olhando, sem piscar, igual criança. Uma rede inteira de fungos que brilha no escuro, debaixo das raízes.

Usa no momento calmo depois dos drones.

## O que acontece depois que você gravar
1. Eu converto cada arquivo com `converter.py` (tom calculado sozinho, modelo mais recente) e te mando para ouvir.
2. Você aprova ou pede nova gravação. Defeitos da conversão **são copiados** para a voz sintética, então só
   aprovo referências limpas.
3. Cada referência aprovada vira um perfil no VoiceStudio ("Lis tensa", "Lis firme"...), com a transcrição.
4. Gero um trecho de teste de cada perfil e comparo com a conversão direta.

## O que não prometo
- **A emoção não é graduada:** o resultado depende de a conversão e o TTS preservarem o seu jeito de falar.
- **O timbre pode variar entre perfis.** Gravar tudo no mesmo dia, com o mesmo microfone, reduz isso.
- **O modelo do RVC ainda está em treino** (época 130 de 300 quando escrevi isto). Dá para gravar já, mas a
  conversão final fica melhor depois que o treino terminar.
