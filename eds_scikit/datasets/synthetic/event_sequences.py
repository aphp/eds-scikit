import datetime

import numpy as np
import pandas as pd

synthetic_event_sequences = {
    "person_id": {
        0: 1,
        1: 1,
        2: 1,
        3: 1,
        4: 1,
        5: 1,
        6: 1,
        7: 1,
        8: 1,
        9: 1,
        10: 1,
        11: 1,
        12: 2,
        13: 2,
        14: 2,
        15: 2,
        16: 2,
        17: 2,
    },
    "event_family": {
        0: "A",
        1: "A",
        2: "B",
        3: "C",
        4: "C",
        5: "D",
        6: "D",
        7: "D",
        8: "E",
        9: "F",
        10: "G",
        11: "G",
        12: "A",
        13: "B",
        14: "C",
        15: "C",
        16: "C",
        17: "D",
    },
    "event": {
        0: "a1",
        1: "a2",
        2: "b1",
        3: "c1",
        4: "c2",
        5: "d1",
        6: "d1",
        7: "d2",
        8: "e1",
        9: "f1",
        10: "g1",
        11: "g1",
        12: "a3",
        13: "b1",
        14: "c3",
        15: "c3",
        16: "c3",
        17: "d1",
    },
    "event_start_datetime": {
        0: "01/01/2020",
        1: "03/01/2020",
        2: "03/01/2020",
        3: "05/01/2020",
        4: "06/01/2020",
        5: "05/01/2020",
        6: "06/01/2020",
        7: "10/01/2020",
        8: "11/01/2020",
        9: "12/01/2020",
        10: "15/01/2020",
        11: "17/01/2020",
        12: "01/01/2020",
        13: "03/01/2020",
        14: "05/01/2020",
        15: "06/01/2020",
        16: "08/01/2020",
        17: "10/01/2020",
    },
    "event_end_datetime": {
        0: "02/01/2020",
        1: "04/01/2020",
        2: "06/01/2020",
        3: np.nan,
        4: "08/01/2020",
        5: "08/01/2020",
        6: "09/01/2020",
        7: "13/01/2020",
        8: np.nan,
        9: "13/01/2020",
        10: "17/01/2020",
        11: "17/01/2020",
        12: "08/01/2020",
        13: "06/01/2020",
        14: "07/01/2020",
        15: "09/01/2020",
        16: "10/01/2020",
        17: "12/01/2020",
    },
}


def load_event_sequences():
    df_events = pd.DataFrame(synthetic_event_sequences)
    df_events.event_start_datetime = pd.to_datetime(
        df_events.event_start_datetime, dayfirst=True
    )
    df_events.event_end_datetime = pd.to_datetime(
        df_events.event_end_datetime, dayfirst=True
    )
    df_events["index_date"] = datetime.datetime(2020, 1, 1)
    return df_events
