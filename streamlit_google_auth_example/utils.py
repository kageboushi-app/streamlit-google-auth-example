import streamlit
from typing import Tuple, List


# https://towardsdatascience.com/creating-multipage-applications-using-streamlit-efficiently-b58a58134030
class MultiPage(List[Tuple[str, int]]):
    def __init__(self, st: streamlit):
        super().__init__()
        self.st = st

    def run(self):
        names = [i[0] for i in self]
        fns = dict(self)
        n = self.st.sidebar.selectbox(
            'Pages',
            names,
        )
        fns[n]()
