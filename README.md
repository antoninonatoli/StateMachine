How to use.

Check the file main_2.py for the use.

Le classi AbcState e AbcTransition sono l'astrazione dei vari stati e transizioni.
Ogni stato concreto dovra' implementare i metodi astratti di AbcState cosi' come ogni transizione concreta dovra' implementare i metodi astratti di AbcTransition.

I file State.py e Transition.py sono esempi di implementazioni per le classi AbcState e AbcTransition.

Nel file main_2.py viene utilizzato un builder design pattern per creare l'oggetto fsm.
fsm implementa il metodo magic __call__ e riceve come parametro un dizionario chiamato context.

In questo esempio viene fornita l'implementazione in cui il contesto contiene una sequenza di numeri interi e si vede se la macchina accetta tale sequenza, raggiungendo pertanto uno stato finale.

Ogni stato viene chiamato durante l'esecuzione e viene eseguita la sua implementazione nel metodo call. Nell'esempio vi sono solo delle print.

Il metodo call sulla fsm viene usato per consentire la totale esecuzione della macchina una volta che tutto l'input e il contesto sono noti a priori.
In caso essi dipendessero da eventi che accadono dopo, durante l'utilizzo, e non sono noti a priori, e' necessario utilizzare l'esempio riportato in main_events.py.

In main.py non viene utilizzato il pattern builder.