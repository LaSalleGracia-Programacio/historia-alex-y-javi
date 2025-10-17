[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/AmxkgJ8C)
# Activitat de Git: “Crea la teva aventura col·laborativa”

## Context
Sou un equip d’escriptors digitals que voleu inventar **una història interactiva**. Cada membre afegirà parts de l’aventura, però com que treballeu junts en el mateix repositori, haureu d’aprendre a **sincronitzar-vos, treballar en branques i resoldre conflictes** quan dueu les idees al text comú.  

El vostre “tauler d’històries” és un repositori de GitHub Classroom creat pel professor. Cada parella té el seu propi repositori compartit.  

---

## Objectius de l’activitat
- Aprendre a clonar i connectar-vos a un repositori remot.  
- Treballar amb branques locals i remotes.  
- Practicar la resolució de conflictes.  
- Adoptar bones pràctiques bàsiques de GitHub: sincronitzar sovint, treballar per branques, fer commits clars.  

---

## Materials inicials
Quan cloneu el vostre repositori trobareu:
- **README.md**: instruccions bàsiques.  
- **story.txt**: el començament de la història.  
- **contributors.md**: fitxer on escriureu els vostres noms.  

---

## Tasques

### 1. Crea el vostre repositori Github amb l'enllaç dels professors
1. Accedeix a l'enllaç dels professors
2. Clona el projecte a local
2. Crea una branca amb el teu nom:  
3. Escriu el teu nom al fitxer `contributors.md`.  
4. Fes commit i puja la branca

---

### 2. Crear la història
1. Generar una història amb IA generativa (GPT, Gemini...) però sense especificar el final de la història
2. Un dels dos developers haurà de guardar la història al fitxer `story.txt`
3. Fes commit i puja els canvis a la teva branca.
4. Fes merge a la main
4. Fes push
5. L'altre developer haurà de fer pull per veure-la

### 3. Primer conflicte: afegim girs inesperats
1. Cada developer a la seva branca, afegiu a `story.txt` **una final sorprenent al final de la història**.  
2. Fes commit i puja els canvis a la teva branca.  
3. Ara integra la teva branca a `main`:  
4. El primer de vosaltres no tindrà problemes. El segon trobarà un **conflicte**.  
5. Resoleu el conflicte junts: editeu `story.txt` perquè la història tingui sentit amb 

---

### 4. Segon repte: ampliem l’aventura
1. Cada membre crea una nova branca:  
2. Afegiu **un paràgraf complet** a la història (no al final, sinó al mig, on vulgueu).  
3. Feu commit i pugeu la branca.  
4. Torneu a `main`, feu `pull` i integreu la nova branca amb `merge`.  
5. Si hi ha conflictes, solucioneu-los parlant i editant el text.  

---

## Reflexió final
- Què ha passat quan heu intentat pujar sense fer `pull`?  
- Què heu après sobre els conflictes?  
- Què us ha ajudat a mantenir la història coherent?  
- Per què és útil treballar amb branques en projectes de programació reals?  
