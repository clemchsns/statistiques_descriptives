import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# Configuration de la page pour qu'elle prenne toute la largeur
st.set_page_config(layout="wide")

# chargement des données
bd_m_detect_A = pd.read_csv("bd_m_detect_A.csv", sep=",")
bd_m_detect_U16 = pd.read_csv("bd_m_detect_U16.csv", sep=",")
bd_m_detect_U17 = pd.read_csv("bd_m_detect_U17.csv", sep=",")
bd_m_detect_U18 = pd.read_csv("bd_m_detect_U18.csv", sep=",")
bd_m_detect_U19 = pd.read_csv("bd_m_detect_U19.csv", sep=",")
bd_m_detect_U20 = pd.read_csv("bd_m_detect_U20.csv", sep=",")
bd_m_detect_U21 = pd.read_csv("bd_m_detect_U21.csv", sep=",")
bd_mU16_U17 = pd.read_csv("bd_mU16_U17.csv", sep=",")
bd_mU16_U18 = pd.read_csv("bd_mU16_U18.csv", sep=",")
bd_mU16_U19 = pd.read_csv("bd_mU16_U19.csv", sep=",")
bd_mU16_U20 = pd.read_csv("bd_mU16_U20.csv", sep=",")
bd_mU16_U21 = pd.read_csv("bd_mU16_U21.csv", sep=",")
bd_mU16_A = pd.read_csv("bd_mU16_A.csv", sep=",")
bd_mU17_U18 = pd.read_csv("bd_mU17_U18.csv", sep=",")
bd_mU17_U19 = pd.read_csv("bd_mU17_U19.csv", sep=",")
bd_mU17_U20 = pd.read_csv("bd_mU17_U20.csv", sep=",")
bd_mU17_U21 = pd.read_csv("bd_mU17_U21.csv", sep=",")
bd_mU17_A = pd.read_csv("bd_mU17_A.csv", sep=",")
bd_mU18_U19 = pd.read_csv("bd_mU18_U19.csv", sep=",")
bd_mU18_U20 = pd.read_csv("bd_mU18_U20.csv", sep=",")
bd_mU18_U21 = pd.read_csv("bd_mU18_U21.csv", sep=",")
bd_mU18_A = pd.read_csv("bd_mU18_A.csv", sep=",")
bd_mU19_U20 = pd.read_csv("bd_mU19_U20.csv", sep=",")
bd_mU19_U21 = pd.read_csv("bd_mU19_U21.csv", sep=",")
bd_mU19_A = pd.read_csv("bd_mU19_A.csv", sep=",")
bd_mU20_U21 = pd.read_csv("bd_mU20_U21.csv", sep=",")
bd_mU20_A = pd.read_csv("bd_mU20_A.csv", sep=",")
bd_mU21_A = pd.read_csv("bd_mU21_A.csv", sep=",")


# Liste des datasets et leurs noms
liste_bd = {
    "Aucune - Equipe de France A": bd_m_detect_A,
    "Aucune - Equipe de France U16": bd_m_detect_U16,
    "Aucune - Equipe de France U17": bd_m_detect_U17,
    "Aucune - Equipe de France U18": bd_m_detect_U18,
    "Aucune - Equipe de France U19": bd_m_detect_U19,
    "Aucune - Equipe de France U20": bd_m_detect_U20,
    "Aucune - Equipe de France U21": bd_m_detect_U21,
    "France U16 - France U17": bd_mU16_U17,
    "France U16 - France U18": bd_mU16_U18,
    "France U16 - France U19": bd_mU16_U19,
    "France U16 - France U20": bd_mU16_U20,
    "France U16 - France U21": bd_mU16_U21,
    "France U16 - France A": bd_mU16_A,
    "France U17 - France U18": bd_mU17_U18,
    "France U17 - France U19": bd_mU17_U19,
    "France U17 - France U20": bd_mU17_U20,
    "France U17 - France U21": bd_mU17_U21,
    "France U17 - France A": bd_mU17_A,
    "France U18 - France U19": bd_mU18_U19,
    "France U18 - France U20": bd_mU18_U20,
    "France U18 - France U21": bd_mU18_U21,
    "France U18 - France A": bd_mU18_A,
    "France U19 - France U20": bd_mU19_U20,
    "France U19 - France U21": bd_mU19_U21,
    "France U19 - France A": bd_mU19_A,
    "France U20 - France U21": bd_mU20_U21,
    "France U20 - France A": bd_mU20_A,
    "France Espoir - France A": bd_mU21_A
}

# liste_bd = [bd_m_detect_A, bd_m_detect_U16, bd_m_detect_U17, bd_m_detect_U18, bd_m_detect_U19, bd_m_detect_U20, bd_m_detect_U21, bd_mU16_U17, bd_mU16_U18, bd_mU16_U19, bd_mU16_U20, bd_mU17_U18, bd_mU17_U19, bd_mU17_U20, bd_mU18_U19, bd_mU18_U20, bd_mU19_U20, bd_mU20_U21, bd_mU21_A]

# Fonction pour créer les graphiques
def create_profil_charts(df):
    df = liste_bd[df]
    
    # Créer deux colonnes pour afficher les graphiques côte à côte
    col1, col2, col3 = st.columns([1, 0.1, 1])
    
    with col1:
        distribution_poste = df["POSTE"].value_counts()
        fig, ax = plt.subplots(figsize=(4, 4))
        colors = plt.cm.Blues([0.2, 0.4, 0.6, 0.8, 1.0])
        distribution_poste.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=colors, ax=ax)
        # met un titre sur le graphique
        ax.set_title("Répartition des postes")
        ax.title.set_fontweight('bold')
        ax.set_xlabel('')
        ax.set_ylabel('')
        ax.axis('equal')
        st.pyplot(fig)

    with col3:
        # st.write("### Répartition des trimestres de naissance")
        df['TRIMESTRE_NAISSANCE'] = pd.cut(df['MOIS_NAISSANCE'], 
                                           bins=[0, 3, 6, 9, 12], 
                                           labels=['T1 (Jan-Mars)', 'T2 (Avr-Juin)', 'T3 (Juil-Sep)', 'T4 (Oct-Déc)'],
                                           right=True)
        distribution_trimestres = df['TRIMESTRE_NAISSANCE'].value_counts()
        fig, ax = plt.subplots(figsize=(4, 4))
        colors = plt.cm.Blues([0.2, 0.4, 0.6, 0.8])
        distribution_trimestres.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=colors, ax=ax)
        ax.set_title("Répartition des trimestres de naissance")
        # met le titre en gras
        ax.title.set_fontweight('bold')
        ax.set_xlabel('')
        ax.set_ylabel('')
        ax.axis('equal')
        st.pyplot(fig)

    # Pôles espoirs et nationalité peuvent rester dans leurs propres colonnes
    # st.write("### Répartition des pôles espoirs")
    col1, col2, col3 = st.columns([1, 0.1, 1])
    with col1:
        distribution_pole = df['POLE_ESPOIR'].value_counts()
        fig, ax = plt.subplots(figsize=(4, 3))
        distribution_pole.plot(kind='bar', color='#4e8eb7', ax=ax)
        ax.set_title("Répartition des 16 pôles espoirs")
        # met le titre en gras
        ax.title.set_fontweight('bold')
        st.pyplot(fig)

    with col3:
        distribution_nationalite = df['NATIONALITE'].value_counts()
        df_nat = pd.DataFrame(distribution_nationalite)
        # Renommer la première colonne en "Nationalité" et la deuxième en "Nombre de joueurs"
        df_nat.columns = ["Nombre de joueurs"]

        st.table(df_nat)
        # fig, ax = plt.subplots(figsize=(4, 3))
        # distribution_nationalite.plot(kind='bar', color='green', ax=ax)
        # ax.set_title("Nationalité des joueurs")
        # # met le titre en gras
        # ax.title.set_fontweight('bold')
        # st.pyplot(fig)


def create_var_jeu_charts(df):
    df_jeu = liste_bd[df]
    
    st.subheader("Performance des joueurs en club")
    # si une colonne commence par "NB_BUT_PAR_MIN_JOUE_PAR_SAISON" ou par "NB_MIN_JOUE_PAR_MATCH_PAR_SAISON" alors on les garde
    df_club = df_jeu[[col for col in df_jeu.columns if col.startswith("NB_BUT_PAR_MIN_JOUE_PAR_SAISON") or col.startswith("NB_MIN_JOUE_PAR_MATCH_PAR_SAISON")]]
    col1 = df_club.columns[0]
    col2 = df_club.columns[1]
    df_club = df_club.rename(columns={col1:"Nombre de but par minutes jouées pour une saison", col2:"Nombre de minutes jouées par match pour une saison"})
    st.write("Moyenne des variables de jeu")
    st.table(df_club.mean())
    # st.table(df_club)


    col1, col2, col3, col4, col5 = st.columns([1,0.1,1,0.1,1])
    with col1:
        if "France U16" in df_jeu.columns:
            st.subheader("Performance des joueurs en équipe de France U16")
            df_U16 = df_jeu[["U16_TITULARISATION","U16_NB_BUT","U16_NB_MIN_JOUE","U16_NB_MATCH_JOUE"]].rename(columns={"U16_TITULARISATION":"Titularisation","U16_NB_BUT":"Nombre de buts","U16_NB_MIN_JOUE":"Nombre de minutes jouées","U16_NB_MATCH_JOUE":"Nombre de matchs joués"})
            # Afficher les moyennes des variables de jeu
            st.write("Moyenne des variables de jeu")
            st.table(df_U16.mean())
            # 
            # st.table(df_U16)
    with col3:
        if "France U17" in df_jeu.columns:
            st.subheader("Performance des joueurs en équipe de France U17")
            df_U17 = df_jeu[["U17_TITULARISATION","U17_NB_BUT","U17_NB_MIN_JOUE","U17_NB_MATCH_JOUE"]].rename(columns={"U17_TITULARISATION":"Titularisation","U17_NB_BUT":"Nombre de buts","U17_NB_MIN_JOUE":"Nombre de minutes jouées","U17_NB_MATCH_JOUE":"Nombre de matchs joués"})
            st.write("Moyenne des variables de jeu")
            st.table(df_U17.mean())

    with col5:
        if "France U18" in df_jeu.columns:
            st.subheader("Performance des joueurs en équipe de France U18")
            df_U18 = df_jeu[["U18_TITULARISATION","U18_NB_BUT","U18_NB_MIN_JOUE","U18_NB_MATCH_JOUE"]].rename(columns={"U18_TITULARISATION":"Titularisation","U18_NB_BUT":"Nombre de buts","U18_NB_MIN_JOUE":"Nombre de minutes jouées","U18_NB_MATCH_JOUE":"Nombre de matchs joués"})
            st.write("Moyenne des variables de jeu")
            st.table(df_U18.mean())

    

    col1, col2, col3, col4, col5 = st.columns([1,0.1,1,0.1,1])
    with col1:
        if "France U19" in df_jeu.columns:
            st.subheader("Performance des joueurs en équipe de France U19")
            df_U19 = df_jeu[["U19_TITULARISATION","U19_NB_BUT","U19_NB_MIN_JOUE","U19_NB_MATCH_JOUE"]].rename(columns={"U19_TITULARISATION":"Titularisation","U19_NB_BUT":"Nombre de buts","U19_NB_MIN_JOUE":"Nombre de minutes jouées","U19_NB_MATCH_JOUE":"Nombre de matchs joués"})
            st.write("Moyenne des variables de jeu")
            st.table(df_U19.mean())
    
    with col3:
        if "France U20" in df_jeu.columns:
            st.subheader("Performance des joueurs en équipe de France U20")
            df_U20 = df_jeu[["U20_TITULARISATION","U20_NB_BUT","U20_NB_MIN_JOUE","U20_NB_MATCH_JOUE"]].rename(columns={"U20_TITULARISATION":"Titularisation","U20_NB_BUT":"Nombre de buts","U20_NB_MIN_JOUE":"Nombre de minutes jouées","U20_NB_MATCH_JOUE":"Nombre de matchs joués"})
            st.write("Moyenne des variables de jeu")
            st.table(df_U20.mean())
    
    with col5:
        if "France U21" in df_jeu.columns:
            st.subheader("Performance des joueurs en équipe de France U21")
            df_U21 = df_jeu[["U21_TITULARISATION","U21_NB_BUT","U21_NB_MIN_JOUE","U21_NB_MATCH_JOUE"]].rename(columns={"U21_TITULARISATION":"Titularisation","U21_NB_BUT":"Nombre de buts","U21_NB_MIN_JOUE":"Nombre de minutes jouées","U21_NB_MATCH_JOUE":"Nombre de matchs joués"})
            st.write("Moyenne des variables de jeu")
            st.table(df_U21.mean())

def affichage_variable(df):
    df_var = liste_bd[df]
    st.write("Voici la liste des variables disponibles dans la base de données sélectionnée")
    st.table(df_var.columns)
    st.write("Voici les premières lignes de la base de données sélectionnée")
    st.table(df_var.head())


# Interface utilisateur
st.title("Analyse des données des joueurs")

# Sélection de la base de données
dataset_selection = st.selectbox("Choisissez une base de données", list(liste_bd.keys()))



# Création des sous-onglets
tab1, tab2, tab3 = st.tabs(["Profil des joueurs", "Variables de jeu","Variables"])

with tab1:
    col1, col2 = st.columns([1, 1])
    with col1:
        create_profil_charts(dataset_selection)

with tab2:
    col1, col2 = st.columns([1, 1])
    with col1:
        create_var_jeu_charts(dataset_selection)

with tab3:
    affichage_variable(dataset_selection)