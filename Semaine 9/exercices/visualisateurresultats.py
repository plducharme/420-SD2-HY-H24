from PySide6.QtWidgets import QMainWindow, QWidget, QTableView, QVBoxLayout
from PySide6.QtCore import QAbstractTableModel, Qt
from typing import Dict
import matplotlib
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
matplotlib.use("qtagg")


class ModeleTable(QAbstractTableModel):
    def __init__(self, resultats: Dict):
        super(ModeleTable, self).__init__()
        self._resultats = resultats

    def data(self, index, role=...):
        if role == Qt.ItemDataRole.DisplayRole:
            ligne_key = list(self._resultats.keys())[index.row()]
            colonne_key = list(self._resultats[ligne_key].keys())[index.column()]
            return self._resultats[ligne_key][colonne_key]

    def rowCount(self, parent=...):
        return len(self._resultats.keys())

    def columnCount(self, parent=...):
        if len(self._resultats.keys()) == 0:
            return 0
        return len(self._resultats[next(iter(self._resultats.keys()))].keys())

    def headerData(self, section, orientation, role=...):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Vertical:
                return str(list(self._resultats.keys())[section])
            if orientation == Qt.Orientation.Horizontal:
                sous_dict = self._resultats[list(self._resultats.keys())[0]]
                return list(sous_dict.keys())[section]


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class VisualisateurResultats(QMainWindow):

    def __init__(self, resultats: Dict):
        super().__init__()
        widget_central = QWidget()
        disposition = QVBoxLayout()
        widget_central.setLayout(disposition)
        self.setCentralWidget(widget_central)

        tableau = QTableView()
        modele = ModeleTable(resultats)
        tableau.setModel(modele)
        disposition.addWidget(tableau)
        mplCanvas = MplCanvas()

        axe_x = list(resultats.keys())
        axes_y = {}
        noms = []

        for nombre_elements, resultats_dict in resultats.items():
            temps_tris = []
            for nom_tri, temps in resultats_dict.items():
                if nom_tri not in noms:
                    noms.append(nom_tri)
                    axes_y[nom_tri] = []
                axes_y[nom_tri].append(temps)

        for nom_tri, temps in axes_y.items():
            mplCanvas.axes.plot(axe_x, temps, label=nom_tri)
            mplCanvas.axes.legend(loc="upper center")
            mplCanvas.axes.set_xlabel("Nombre éléments")
            mplCanvas.axes.set_ylabel("Temps")

        disposition.addWidget(mplCanvas)
        self.setWindowTitle("Résultats des comparaisons de tris")







