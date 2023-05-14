# Programimi i SBoxa-ve dhe gjenerimi i 16 subkeys nga çelësi 64 bitesh tek DES algoritmi
## Anëtaret e grupit: Roni Kukaj, Suhejl Vejseli, Rron Sherifi
## Gjuha programuese: Python


### Ky repository përmban kod në gjuhën progrmauese Python i cili fokusohet në programimin e S-boxave dhe gjenerimin e 16 subkeys për secilin round të algoritmit DES. DES algoritmi është një algoritëm simetrik i enkriptimit i cili operon në blloqe të dhenash 64-bit. Feistel Cipher është një algoritëm simetrik enkriptimi që ndan tekstin e thjeshtë në blloqe dhe aplikon raunde të shumta transformimesh për të enkriptuar ose dekriptuar të dhënat.
## Struktura e kodit
### SubKeyGenerator: Kjo klasë është përgjegjëse për gjenerimin e 16 subkeys të përdorur në çdo raund të algoritmit DES.
### SBoxes: Kjo klasë përmban S-boxat që përdoren ne DES algoritmin. Qëllimi i tyre është të transformojnë 48-bit input ne 32-bit output.
### FeistelCipher: Kjo klasë përmban operacionet e enkriptimit dhe dekriptimit të algoritmit DES. Ai përdor S-boxat dhe subkeys të gjeneruar nga klasa SubKeyGenerator për të kryer strukturën e FeistelCipher, e cila përpunon në mënyrë të përsëritur të dhënat hyrëse përmes raundeve të shumta.
### Implementimin e algoritmit e kemi bërë duke përdorur Python OOP, në një file kemi shkruar klasat bazë që kryejnë funksionet e nevojshme gjatë enkriptimit/dekriptimit. Në Main klasën kemi përdorur një librari për GUI të python që të vizualizojmë punën e këtij algoritmi dhe ta bejmë më të lehtë për prezentim.

### Per GUI kemi përdorur librarinë e Python, PyQt5 e cila me anë të Programimit të Orientuar në Objekte na ka mundësuar që të dizajnojmë pjesën FrontEnd të projektit tonë. Kemi përdorur dy tabs, një për encryption dhe një tjetër për decryption, te cilat kryejnë funksionet përkatëse.