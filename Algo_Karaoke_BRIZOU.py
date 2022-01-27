"""
Bienvenue dans le Karaoke
Le karaoke contient actuellement 5 musiques
Pour chaque joueur, il est possible d'avoir un surnom, un score, la moyenne de ses scores, le total de ses scores, son meilleur score, son pire score et il est aussi possible d'ajouter un score
(La partie qui suit est dédiée à la partie A du sujet)
"""


class Player:                                            #Je commence par définir ma classe Player qui contiendra toutes mes méthodes inscrites dans le diagramme de classe

    def __init__(self,pseudo,score):                     #La première méthode à venir est "__init__" elle est présente à chaque début de classe et permet d'initialiser les attributs qui suivront
        self.__pseudoPlayer=pseudo                       #Ayant défini "pseudo" et "score" comme paramétres de ma méthode __init__, je me dois de les initaliser et de rajouter 2 underscores afin de valider
        self.__scorePlayer=score                         #Que ce sont bien des paramètres non modifiables

    def getPseudoPlayer(self):                           #Ensuite, la méthode getPseudoP permet de retourner le surnom du joueur actuel
        return self.__pseudoPlayer                      

    def getScorePlayer(self):                            #La méthode getScoreP permet de retourner son score
        return self.__scorePlayer

    def afficherScore(self,cle):                         #Cette méthode permet de retourner le score d'un joueur de la partie
        return self.getScorePlayer()[cle]

    def moyenneScore(self):                              #Il est possible de calculer automatiquement la moyenne de ses scores enregistrés
        moyenne=0
        for cle, valeur in self.getScorePlayer().items():
            moyenne = moyenne+valeur                     #On commence par additionner tous les scores entre eux
        moyenne = moyenne/5                              #Pour calculer, on divise par 5 car le karaoke contient (pour le moment) 5 musiques, mais rien n'empêche de pouvoir rajouter des musiques, il faudra simplement modifier le "5"
        return moyenne

    def totalScore(self):                                #Il est aussi possible de calculer automatiquement son score total
        total=0
        for cle, valeur in self.getScorePlayer().items():
            total = total+valeur                         #Pour cela, rien de compliqué, il suffit d'additionner tous les scores entre eux
        return total

    def meilleurScore(self):                             #Cette méthode permet de retrouver et afficher le meilleur score du joueur, invitant alors le joueur à toujours se surpasser et effectuer un meilleur score
        meilleurScore=0
        cleScore=0
        for cle, valeur in self.getScorePlayer().items():
            if valeur>meilleurScore:
                meilleurScore=valeur
                cleScore=cle
        print("le meilleur score est: ",meilleurScore, " sur la musique: ", cleScore, " Bravo !")

    def pireScore(self):                                #Il est aussi possible de calculer le pire score qui a été effectué pour le moment et affiche aussi la musique concernée
        pireScore=100
        cleScore=0
        for cle, valeur in self.getScorePlayer().items():
            if valeur<pireScore:                        #On parcourt les scores du joueur, et, si on trouve un score inférieur à celui stocké dans la variable pireScore, dans ce cas, on écrase la valeur stockée
                pireScore=valeur      
                cleScore=cle
        print("l'actuel pire score est: ",pireScore, " effectué sur la musique: ", cleScore)

    def ajouterScore(self,cle,score):                   #Il est aussi possible d'ajouter un score
        self.getScorePlayer()[cle]=score
        print("Le score de",score," points à bien été ajouter")

"""
Ceci représente la base de mon programme, c'est ici que je vais inscrire les musiques disponibles à ce jour
Ensuite, j'y ajoute la liste des joueurs disponibles, cependant, je leur attribue un score de base sur chaque musique
Pour rappel : 
- Le meilleur score qui peut être obtenu est 100/100
        Aucun joueur ne peut donc dépasser ce score
- Le pire score qui peut être obtenu est 50/100 
        Aucun joueur ne peut obtenir un score inférieur OU sinon, cela veut dire que la musique n'a oas encore été jouée
"""
score1={"musique1":60, "musique2":0, "musique3":80, "musique4":90, "musique5":70}
score2={"musique1":50, "musique2":80, "musique3":100, "musique4":0, "musique5":60}
score3={"musique1":0, "musique2":100, "musique3":50, "musique4":0, "musique5":0}
joueur1= Player("Joueur1",score1)
joueur2= Player("Joueur2",score2)
joueur3= Player("Joueur3",score3)
joueur1.moyenneScore()
joueur1.totalScore()
joueur1.meilleurScore()
joueur1.pireScore()
joueur1.ajouterScore(2,10)

"""
Nous venons de finir la programmation de la classe Joueur (Player)
Or, tout cela ne signifie rien, si cela ne repose par sur un pilier, nous n'avons que des méthodes sans réelle signification
Pour pouvoir réellement jouer au Karaoke, il nous faut ajouter une classe Karaoke
(La partie qui suit est dédiée à la partie B du sujet)
"""

class Karaoke:                                      #Je commence par définir ma classe Karaoke qui contiendra toutes mes méthodes inscrites dans le diagramme de classe

    def __init__(self,listJoueur,listChanson):      #Comme convenu, je dèbute par ma méthode "__init__" 
        self.__listJoueurKaraoke=listJoueur         #Cette fois-ci, les joueurs(euses) sont identifié(e)s par l'appelation "JoueurKaraoke" permettant de les différencier de la classe Joueur(Player)
        self.__listChansonKaraoke=listChanson

    def getJoueur(self):                            #La méthode getJoueur permet de donner le nom du joueur 
        return self.__listJoueurKaraoke

    def getChanson(self):                           #La méthode getChanson permet de donner le nom de la musique
        return self.__listChansonKaraoke

    def ajouterJoueur(self,joueur):                 #Cette méthode permet d'ajouter un joueur, elle contient le paramètre "joueur" qui nous permet de pouvoir agir directement sur la méthode getJoueur et donc d'agir sur la liste de joueurs(euses)
        self.getJoueur().append(joueur)
        print("le joueur a bien été ajouter")

    def supprimerJoueur(self,joueur):               #Cette méthode permet de supprimer un joueur
        if self.getJoueur <= 1:                     #On fait attention a l'exception ou il ne resterait plus qu'un joueur, car le jeu ne fonctionnerait pas s'il n'y avait pas au minimum 1 joueur
            print("Désolé, ce n'est pas possible, il faut 1 joueur minimum, or il ne reste que :", karaokeTest.getJoueur())
        else:
            self.getJoueur().remove(joueur)
            print("le joueur a bien été supprimer")

    def meilleurScoreChanson(self,chanson):         #Cette méthode est un peu plus compliquée, on doit comparer tout les scores effectuées sur une même musique pour pouvoir extraire le meilleur d'entre-eux
        valeur=0
        meilleureValeur=0
        for i in range (len(self.getJoueur())):     #Pour chaque joueur, on effectue les opérations suivantes
            valeur = self.getJoueur()[i].afficherScore(chanson)
            if valeur>meilleureValeur:
                meilleureValeur=valeur
        print("Le meilleur score de cette musique est: ",meilleureValeur)
        if meilleureValeur < 100:
            print("Vous pouvez faire mieux !")

    def meilleurScoreTotal(self):                    #On fait de même sauf que cette fois, on parcourt tout les scores des joueurs
        valeurScore=0
        plusGrandScore=0
        for i in range (len(self.getJoueur())):
            valeurScore=self.getJoueur()[i].totalScore()
            if valeurScore>plusGrandScore:
                plusGrandScore=valeurScore
        print("Le meilleur score général est: ",plusGrandScore)

    def meilleurMoyenne(self):                      #Pour finir, on calcule la meilleure moyenne atteinte jusqu'ici
        moyennej=0
        plusGrandemoyenne=0
        for i in range (len(self.getJoueur())):
            moyennej=self.getJoueur()[i].moyenneScore()
            if moyennej>plusGrandemoyenne:
                plusGrandemoyenne=moyennej
        print("La meilleure moyenne est: ",plusGrandemoyenne)


"""
Pour terminer, cela représente l'essence-même de ma classe Karaoke
Cela me permet de tester chacunes des fonctions qui sont ci-dessus
"""

listJoueur=["j1","j2"]
listChanson=["musique1","musique2","musique3","musique4","musique5"]
karaokeTest= Karaoke(listJoueur,listChanson)
karaokeTest.ajouterJoueur("j3")
print("Voici la liste des joueurs", karaokeTest.getJoueur())
#karaokeTest.meilleurScoreChanson("musique1")
#karaokeTest.meilleurScoreTotal()
#karaokeTest.meilleurMoyenne()
karaokeTest.supprimerJoueur("j3")
print("Voici la liste des joueurs restants", karaokeTest.getJoueur())