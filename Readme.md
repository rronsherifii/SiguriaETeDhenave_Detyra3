# Programimi i SBoxa-ve dhe gjenerimi i 16 subkeys nga celesi 64 bitesh tek DES algoritmi
## Anetaret e grupit: Roni Kukaj, Suhejl Vejseli, Rron Sherifi
## Gjuha programuese: Python


### Ky repository përmban kod në gjuhën progrmauese Python i cili fokusohet në programimin e S-boxave dhe gjenerimin e 16 subkeys për secilin round të algoritmit DES. DES algoritmi është një algoritëm simetrik i enkriptimit i cili operon në blloqe të dhenash 64-bit. Feistel Cipher është një algoritëm simetrik enkriptimi që ndan tekstin e thjeshtë në blloqe dhe aplikon raunde të shumta transformimesh për të enkriptuar ose dekriptuar të dhënat.
## Struktura e kodit
### SubKeyGenerator: Kjo klasë është përgjegjëse për gjenerimin e 16 subkeys të përdorur në çdo raund të algoritmit DES.
### SBoxes: Kjo klasë përmban S-boxat që përdoren ne DESS agoritmin. Qëllimi i tyre është të transformojnë 38-bit input ne 32-bit output.
### FeistelCipher: Kjo klasë përmban operacionet e enkriptimit dhe dekriptimit të algoritmit DES. Ai përdor S-boxat dhe nënçelësat e gjeneruar nga klasa SubKeyGenerator për të kryer strukturën e FeistelCipher, e cila përpunon në mënyrë të përsëritur të dhënat hyrëse përmes raundeve të shumta.
### Implementimin e algoritmit e kemi bere duke perdorur Python OOP, ne nje file kemi shkruar klasat baze qe kryejne funksionet e nevojshme gjate enkriptimit/dekriptimit. Ne dy file tjera kemi thirrur funksionalitet per encryption dhe decryption. Ndersa ne file te fundit kemi perdorur nje librari per GUI te python qe te vizualizojme punen e ketij algoritmi dhe ta bejme me te lehte per prezentim.

### Per GUI kemi perdorur librarine e Python, PyQt5 e cila me ane te Programimit te Orientuar ne Objekte na ka mundesuar qe te dizajnojme pjesen FrontEnd te projektit tone. Kemi perdorur dy tabs, nje per encryption dhe nje tjeter per decryption, te cilar kryejne funksionet perkatese.