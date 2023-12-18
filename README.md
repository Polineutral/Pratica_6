# Pratica_6
Nessa prática, foram utilizadas as bibliotecas mfrc522 e OpenCV, juntamente com as bibliotecas time, os e RPi.GPIO para construir dois circuitos:

## Leitor de Tag RFID
O primeiro sendo de leitura do ID de uma tag RFID, no qual uma mensagem de texto será apresentada na tela e um LED verde acenderá caso o ID da tag seja o correto. Caso o ID não seja o correto, uma mensagem na tela indicará e um LED vermelho irá acender. Abaixo estão as imagens da montagem e funcionamento do circuito:

<img src="/Imagens/RFID/Montagem_RFID.jpeg">  Imagem da montagem do circuito.

<img src="/Imagens/RFID/Tag_autorizado.jpg">  Imagem do LED verde aceso com o tag correto.

<img src="/Imagens/RFID/Tag_nao_autorizado.jpg">  Imagem do LED vermelho aceso com o tag incorreto.

## Câmera com Reconhecimento Facial
O segundo projeto desenvolvido foi um circuito utilizando uma câmera para reconhecimento facial. O programa foi configurado para guardar uma foto toda vez que detectar um rosto, cortando o restante da imagem, enquanto salva apenas o rosto detectado. Para mostrar que um rosto foi detectado, o programa desenha um retângulo verde em volta do rosto detectado na imagem da câmera sendo mostrada na interface da RaspberryPi. Além disso, foi feita uma montagem de forma a possibilitar que, ao pressionar um botão, a câmera guarda a imagem atual em um diretório, diferente do diretório onde os rostos detectados estão sendo salvos, possibilitando tirar fotos do que for desejado. Abaixo temos uma foto da montagem e um exemplo de foto tirada pelo reconhecimento facial e um exemplo de foto tirada ao pressionar o botão:

<img src="/Imagens/Câmera/Montagem_câmera.jpg">  
Imagem da montagem do circuito.


<img src="/Imagens/Câmera/face_1701715982.jpg">  
Foto tirada pelo reconhecimento facial do projeto.


<img src="/Imagens/Câmera/fotinhu_1701715984.jpg">  
Foto tirada ao pressionar o botão.
