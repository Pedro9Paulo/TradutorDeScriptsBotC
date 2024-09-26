# TradutorDeScriptsBotC

1- Rode o executável tradutorBotC.exe para Selecionar e traduzir os Scripts desejados (ou o tradutorBotC.py para Mac e Linux com python).

2- Para aqueles com python rode o jsontransall.py para traduzir todos os Scripts na pasta ingles para a pasta ptbr.

## Pra quem for editar
- images pasta com os pngs dos personagens, incluindo os 2 alinhamentos e a padão (no caso de viajantes)
- ptbr/all.json contém todas as roles traduzidas, qualquer mudança na traduções deve ser feita nesse arquivo.
- ordem.py contém a ordem da noite, qualquer mudança deve ser feita nesse arquivo e roda-lo para atualizar no ptbr/all.json
- tradutorBotc.py versão python do executável
- tradutor.py contém as função que de fato traduzem, chamadas pelo tradutorBotC.py e o jsontransall.py
- tradutorWeb.py app Flask que cria a página da Web com o tradutor (atualmente hosteado em https://pedro9paulo.pythonanywhere.com/, mas não funciona totalmente)

## Para criar o executável
1- Instale o pyinstaller
2- Rode ```pyinstaller tradutorBotC.py```
3- Rode ```pyinstaller --onedir --add-data "ptbr\all.json";"ptbr" tradutorBotC.py```
4- Rode ```pyinstaller -F -w --add-data "ptbr\all.json";"ptbr" tradutorBotC.py```

### O que significa cada chave no json das roles
- **id**: Identificador do personagem, padrão de nome: id original (sem underline) + \_br
- **image**: Lista com link de imagens dos personagem; em caso de residentes a primeira imagem deve ser a padrão e a segundo do alinhamento oposto, já viajantes devem ser a padrão, do bem e do mau
- **name**: Nome traduzido do personagem
- **edition**: Edição do personagem, para personagens experimentais, enquanto eles não tem edição esse campo é vazio.
- **team**: O tipo do personagem; **"townsfolk"** se for Cidadão, **"outsider"** se for Forasteiro, **"minion"** se for Lacaio, **"demon"** se for Demônio, **"traveler"** se for Viajante e **"fabled"** se for Lenda.
- **firstNight**: Lugar na ordem da noite da primeira noite, não editar essa parte, usar o ordem.py, ao criar novos personagens coloque qualquer número de placeholder antes de rodar o ordem.py
- **firstNightReminder**: Tradução do texto que aparece na ficha da primeira noite pro narrador desse personagem **:reminder:** cria as bolinhas.
- **otherNight**: Lugar na ordem da noite das outras noite, não editar essa parte, usar o ordem.py, ao criar novos personagens coloque qualquer número de placeholder antes de rodar o ordem.py
- **otherNightReminder**: Tradução do texto que aparece na ficha das outras noites pro narrador desse personagem :reminder: cria as bolinhas.
- **reminders**: Lista com a tradução de cada marcador do personagem (marcadores repetidos devem ser mais de uma vez).
- **remindersGlobal**: Lista com a tradução de cada marcador Global (que podem ser usados mesmo que ninguém tenha o token de tal personagem) do personagem .
- **setup**: **true** se o personagem tem uma habilidade que altera o set up do jogo, **false** caso contrário.
- **ability**: Tradução do texto da habilidade do Personagem.
- **special**: Lista de funcionalidades especiais dos personagens. (ver funcionalidades na próxima secção)
- **jinxes**: Lista de jinxes do personagem; um jinx contém duas entradas de chave-valor (entre {}): o **id** do outro personagem do jinx e o **reason** que contém a tradução do texto do jinx. (o jinx deve aparecer na definição de apenas 1 dos 2 personagens).

### Funcionalidades especiais
As funcionalidades especiais usam formato chave-valor (entre {}) e são formadas pela combinação das chaves **"type"** e **"name"** onde **"type"** indica o que a funcionalidade afeta e **"name"** é a funcionalidade específica. Dependendo da funcionalidade pode ser necessário adicionar argumentos adicionais através das chaves **"time"**, **"value"** e **"global"**

- **"type"**: indica aonde a funcionalidade tem efeito, seu valores podendo ser: **"selection"**: na seleção de personagens, **"signal"**: opções nas mensagens entre narrador e jogador, **"vote"**: durante a votação, **reveal"**: duarante a revelação do grimório, **"ability"**: para habilidades que devem ser manualmente atividas

**"time"**: momento do jogo onde a funcionalide tem efeito opções sendo: **"pregame"**: antes de enviar os personagens, **"day"**: durante a fase do dia, **"night"**: durante a fase da noite, **"firstNight"**: durante especificamente a primeira noite, **"firstDay"**: durante especificamente o primeiro dia, **"otherNight"**: durante a fase da noite exceto a primeira, **"otherDay"**: durante a fase do dia esceto o primeiro

**"value"**: Qualquer número ou texto usado como parâmetro para as habilidades

**"global"**: O tipo de personagem (**"townsfolk"** para Cidadão, **"outsider"** para Forasteiro, **"minion"** para Lacaio, **"demon"** para Demônio) que recebe a habilidade marcada invés de todo mundo ou apenas quem tem o token, é uma gambiarra para fazer o Monstrim funcionar mesmo sem ninguém tecnicamente ser tal personagem, não recomendado usar pelos desenvolvedores pois está passivel de mudança (mas obviamente usamos para fazer a tradução do Monstrim). Os tipos são:

**"name"**: identificador da habilidade em si veja na tabela abaixo todas elas

#### Funcionalidades que alteram o votações (**"type": "vote"**)

| **"name"** | **"type"** | **"value"** | **"time""** | **"global"** | Funcionalidade | exemplo de papel | 
| --- | --- | --- | --- | --- | -------------------- | ----- |
| **"bag-disable"** | **"selection"** | sem efeito | sem efeito | sem efeito | Impede de selecionar o personagem | Marionete |
| **"bag-duplicate"** | **"selection"** | sem efeito | sem efeito | sem efeito | Possibilita selecionar múltiplos do personagem | Legião |
| **"grimoire"** | **"signal"** | sem efeito | Opcional | Opcional | Possibilita o narrador enviar um Grimório ao jogador | Espião |
| **"card"** | **"signal"** | Texto | Opcional| Opcional | Cria botão customizado com o conteúdo em **"value"** para o narrador mandar ao jogador | Mezéfeles |
| **"player"** | **"signal"** | Texto | Opcional | Opcional | Cria botão customizado com o conteúdo em **"value"** para o jogador mandar ao narrador | Não Utilizado |
| **"hidden"** | **"vote"** | sem efeito | sem efeito | sem efeito | Apenas o narrador consegue ver as mãos levantadas e o resultado de uma votação | Realejo |
| **"multiplier"** | **"vote"** | Número | sem efeito | sem efeito | O voto do jogador marcado com o marcador do personagem é multiplicado pelo valor em **"value"** | Ladrão |
| **"replace-character"** | **"reveal"** | sem efeito | sem efeito | sem efeito | O primeiro marcador em **"remindersGlobal"** do personagem substitui o personagem da pessoa marcada na revelação do Grimório | Filósofo |
| **"pointing"** | **"ability"** | sem efeito | Opcional | Opcional | Da ao jogadores a opção de apontar para outros jogadores | Homem-Bomba |
| **"ghost-votes"** | **"ability"** | sem efeito | Opcional | sem efeito | Devolve os votos de todos os jogadores mortes que o utilizaram | Barqueiro |
| **"distribute-roles"** | **"ability"** | sem efeito | Opcional | sem efeito | Envia os personagens atribuidos aos jogadores, para os jogadores | Homem-Bomba |