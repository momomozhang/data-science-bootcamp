import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# Design/Layout Basics
st.set_page_config(page_title="DAX App", layout="wide")


# Lädt Daten in session state und dann in Variable
@st.cache_data
def load_data():
    return pd.read_csv("DAXDataStreamlit.csv")


data = load_data()


#####################################################################################################
# Sidebar
st.sidebar.header("Sidebar")
st.sidebar.write("Hier kannst du die zu analysierenden Aktien auswählen:")

selected_stocks = st.sidebar.pills(
    "Auswahl", data.iloc[:, 1].drop_duplicates(), selection_mode="multi"
)

# Erstellt Arbeitskopie der Daten
filtered_data = data
# Entfernt Zeitzone durch String-Konversion und Slicing nach den ersten 11 Zeichen
filtered_data["Date"] = filtered_data["Date"].astype(str).str[:10]
# Transformiert zu maschinen-freundlichem Datetime-Format
filtered_data["Date"] = pd.to_datetime(filtered_data["Date"], errors="coerce")

# Extrahiert erstes/letztes Datum für Zeit-Slider
first_date = filtered_data["Date"].min().to_pydatetime()
last_date = filtered_data["Date"].max().to_pydatetime()

# Erzeugt Dataframe, der nur Zeilen der ausgewählten Aktien beinhaltet (Angenommen zweite Spalte enthält die Namen d. Aktien)
stock_filtered_data = filtered_data[data.iloc[:, 1].isin(selected_stocks)]


#################################################################################################################
# Popover für Zeit-Einstellungen
with st.popover("Zeit-Einstellungen"):
    date_range = (first_date, last_date)
    if selected_stocks:
        # Erzeugt einen Slider für den Zeitrahmen
        selected_date_range = st.slider(
            "Wähle den Zeitraum aus:",
            min_value=first_date,
            max_value=last_date,
            value=date_range,  # Setzt den Zeitrahmen standardmäßig auf den vollständigen Zeitraum
            format="YYYY-MM-DD",
            step=pd.Timedelta(
                weeks=1
            ).to_pytimedelta(),  # Ensure the slider moves in one-week steps
        )

with st.popover("Metrik-Auswahl"):
    metric = st.selectbox(
        "Wähle die darzustellende Metrik", ["Open", "High", "Low", "Close", "Volume"], index=3
    )

if selected_stocks:
    # Adapt the used date range based on slider selection
    stock_filtered_data = stock_filtered_data[
        (stock_filtered_data["Date"] >= selected_date_range[0])
        & (stock_filtered_data["Date"] <= selected_date_range[1])
    ]

######################################################################################################
# Graph/Hauptteil
st.header("Projekt DAX-Analyse")
"Mit dieser App kannst du die letzten **sechs Monate** des DAX analysieren. :chart:"


col1_graph, col2_tools = st.columns([2, 1])


with col1_graph:
    st.write("")  # Für die Optik
    if selected_stocks:
        fig, ax = plt.subplots(figsize=(10, 6))

        # Gruppiert nach Datum und plotted jede gewählte Aktie
        for stock in selected_stocks:
            stock_data = stock_filtered_data[stock_filtered_data.iloc[:, 1] == stock]
            ax.plot(
                stock_data.iloc[:, 2], stock_data.loc[:, metric], label=stock
            )  # Assuming last column is the stock price

        # Graph Konfiguration
        ax.xaxis.set_major_locator(mdates.MonthLocator())  # Show ticks at the start of each month
        ax.xaxis.set_major_formatter(
            mdates.DateFormatter("%Y-%m-%d")
        )  # Format ticks as 'Year-Month'
        plt.xticks(rotation=45)  # Rotiert x-Achsen Labels für Lesbarkeit
        ax.set_title("Aktienpreise im Zeitverlauf")
        ax.set_xlabel("Datum")
        ax.set_ylabel("Preis [€]")
        ax.legend()
        ax.grid(True)
        plt.tight_layout()

        # Zeigt den Graphen für die ausgewählten Aktien
        st.pyplot(fig)

    else:
        st.write("Wähle Aktien aus der Sidebar aus um Analysen durchzuführen!")

    if st.toggle("Dataframe anzeigen:"):
        st.dataframe(stock_filtered_data)


with col2_tools:
    st.header("Analyse-Tools")

    if selected_stocks:
        st.subheader("Statistiken")

        for stock in selected_stocks:
            stock_data = stock_filtered_data[stock_filtered_data.iloc[:, 1] == stock]

            if not stock_data.empty:
                st.write(f"**{stock}**")

                current_value = stock_data[metric].iloc[-1]
                start_value = stock_data[metric].iloc[0]
                min_value = stock_data[metric].min()
                max_value = stock_data[metric].max()
                avg_value = stock_data[metric].mean()

                change = current_value - start_value
                change_percent = (change / start_value) * 100

                col_a, col_b = st.columns(2)
                with col_a:
                    st.metric("Aktuell", f"{current_value:.2f} €")
                    st.metric("Min", f"{min_value:.2f} €")
                    st.metric("Max", f"{max_value:.2f} €")
                with col_b:
                    st.metric("Durchschnitt", f"{avg_value:.2f} €")
                    st.metric("Veränderung", f"{change:.2f} €", f"{change_percent:.2f}%")

                st.divider()

        st.subheader("Vergleich")

        performance_data = []
        for stock in selected_stocks:
            stock_data = stock_filtered_data[stock_filtered_data.iloc[:, 1] == stock]
            if not stock_data.empty:
                start = stock_data[metric].iloc[0]
                end = stock_data[metric].iloc[-1]
                perf = ((end - start) / start) * 100
                performance_data.append({"Aktie": stock, "Performance (%)": perf})

        if performance_data:
            perf_df = pd.DataFrame(performance_data).sort_values("Performance (%)", ascending=False)
            st.dataframe(perf_df, hide_index=True)

            best = perf_df.iloc[0]
            worst = perf_df.iloc[-1]

            st.success(f"🏆 Beste: {best['Aktie']} ({best['Performance (%)']:.2f}%)")
            st.error(f"📉 Schlechteste: {worst['Aktie']} ({worst['Performance (%)']:.2f}%)")

    else:
        st.info("Wähle Aktien aus, um Analysen zu sehen.")
