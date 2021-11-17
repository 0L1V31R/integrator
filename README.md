# Projeto Integrador

Projeto de um leitor de RFID integrado ao Raspberry PI, as TAG que serão lida devem estar associadas ao nome de um aluno,
essas TAG serão instaladas em uma pulseira junto com ESP32 conectado aum sensor de temperatura - LM35, este fará o monitoramento
da temperatura do aluno e encaminhará via bluetooh para raspberry.

Aqui estão a programação do leitor, que será instalado na raspberry e apresentará o nome do aluno em função da TAG associada ao RFID bem como a sua temperatura corpórea. Haverá uma lógica associada:

1. Caso o RFID não esteja associado ao aluno, exibir informação da tela em vermelho
2. Caso a temperatura do aluno seja superior a 36 graus Célsius, o fundo deve ficar vermelho;
3. Caso a temperatura do aluno seja menor ou igual a 36 graus Célsius, mas o aluno tenha alguma pendencia, o fundo deve ficar em amarelo
4. Caso a temperatura do aluno seja menor ou igual a 36 graus Célsius e sem pendencias o fundo deve ficar na cor verde.

_O que estou utilizando:_
- RASPBERRY PI 4:
-- Leitor RFID
-- Python 3.9
-- Flask

-ESP32:
-- C++
