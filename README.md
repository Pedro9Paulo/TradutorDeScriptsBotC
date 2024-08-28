# TradutorDeScriptsBotC

1- Rode o jsontransall.py para traduzir todos os Scripts na pasta ingles para a pasta ptbr.

2- Para Traduzir um script só rode jsontrans.py e insira o nome do script no linha de comando.

## Pra quem for editar
- images pasta com os pngs dos personagens, incluindo os 2 alinhamentos e a padão (no caso de viajantes)
- ptbr/all.json contém todas as roles traduzidas, qualquer mudança na traduções deve ser feita nesse arquivo.
- ordem.py contém a ordem da noite, qualquer mudança deve ser feita nesse arquivo e roda-lo para atualizar no ptbr/all.json

### O que significa cada chave no json das roles
- **id**: Identificador do personagem, padrão de nome: id original (sem underline) + \_br
- **image**: Lista com link de imagens dos personagem; em caso de residentes a primeira imagem deve ser a padrão e a segundo do alinhamento oposto, já viajantes devem ser a padrão, do bem e do mau
- **name**: Nome traduzido do personagem
- **edition**: Edição do personagem, para personagens experimentais, enquanto eles não tem edição esse campo é vazio.
- **team**: O tipo do personagem; "townsfolk" se for Cidadão, "outsider" se for Forasteiro, "minion" se for Lacaio, "demon" se for "Demônio", "traveler" se for Viajante e "fabled" se for "Lenda".
- **firstNight**: Lugar na ordem da noite da primeira noite, não editar essa parte, usar o ordem.py, ao criar novos personagens coloque qualquer número de placeholder antes de rodar o ordem.py
- **firstNightReminder**: Tradução do texto que aparece na ficha da primeira noite pro narrador desse personagem :reminder: cria as bolinhas.
- **otherNight**: Lugar na ordem da noite das outras noite, não editar essa parte, usar o ordem.py, ao criar novos personagens coloque qualquer número de placeholder antes de rodar o ordem.py
- **otherNightReminder**: Tradução do texto que aparece na ficha das outras noites pro narrador desse personagem :reminder: cria as bolinhas.
- **reminders**: Lista com a tradução de cada marcador do personagem (marcadores repetidos devem ser mais de uma vez).
- **remindersGlobal**: Lista com a tradução de cada marcador Global (que podem ser usados mesmo que ninguém tenha o token de tal personagem) do personagem .
- **setup**: *true* se o personagem tem uma habilidade que altera o set up do jogo, *false* caso contrário.
- **ability**: Tradução do texto da habilidade do Personagem.
- **special**: Lista de funcionalidades especiais dos personagens. (ver funcionalidades na próxima secção)
- **jinxes**: Lista de jinxes do personagem; um jinx contém duas chaves: o **id** do outro personagem do jinx e o **reason** que contém a tradução do texto do jinx. (o jinx deve aparecer na definição de  apenas 1 dos 2 personagens).

#### Funcionalidades especiais
| Funcionalidade | Como usar | exemplo de papel |
| ---------------| --------- | ---------------- |
| Receber o Grimório como informação | { "name": "grimoire", "type": "signal", "time": "night"} | Espião |
| Modificar o valor de um voto | { "name": "multiplier", "type": "vote", "value": número que quers multiplicar o voto}| Ladrão |
| Substituir o token na revelação do grimório pelo Marcador Global neste jogador| { "name": "replace-character", "type": "reveal"} | Bêbado |
| Permitir colocar mais de um personagem deste token na distribuição de Personagens | { "name": "bag-duplicate", "type": "selection"} | Legião |
| Mãos levantadas não aparecerem durante a votação | { "name": "hidden", "type": "vote"} | Realejo 
| Possibilidade dos jogadores apontarem para outros jogadores (restrito há um tipo de personagem se global presente)| { "name": "pointing", "type": "ability", "time": "day" ou "night", global: (opcional) tipo de personagem afetado} | Homem-Bomba |
