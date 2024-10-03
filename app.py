# # """
# # # My first app
# # Here's our first attempt at using data to create a table:
# # """

# # import streamlit as st
# # import pandas as pd
# # df = pd.DataFrame({
# #   'first column': [1, 2, 3, 4],
# #   'second column': [10, 20, 30, 40]
# # })

# # df


# # st.write("Here's our first attempt at using data to create a table:")
# # st.write(pd.DataFrame({
# #     'first column': [1, 2, 3, 4],
# #     'second column': [10, 20, 30, 40]
# # }))

# # import streamlit as st
# # import numpy as np

# # dataframe = np.random.randn(10, 20)
# # st.dataframe(dataframe)

# import streamlit as st
# import numpy as np
# import pandas as pd

# dataframe = pd.DataFrame(
#     np.random.randn(10, 20),
#     columns=('col %d' % i for i in range(20)))

# st.dataframe(dataframe.style.highlight_max(axis=0))

# import streamlit as st
# import numpy as np
# import pandas as pd

# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

# st.line_chart(chart_data)

# import streamlit as st
# import numpy as np
# import pandas as pd

# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])
# st.write('This is a map of the San Fransisco area')
# st.map(map_data)
#sliders
import streamlit as st

start_color, end_color = st.select_slider(
    "Select a range of color wavelength",
    options=[
        "Red",
        "Orange",
        "Yellow",
        "Green",
        "Blue",
        "Indigo",
        "Violet",
    ],
    value=("Red", "Blue"),
)
st.write("You selected wavelengths between", start_color, "and", end_color)
#button
import streamlit as st

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

#Icons on buttons

import streamlit as st

left, middle, right = st.columns(3)
if left.button("Plain button", use_container_width=True):
    left.markdown("You clicked the plain button.")
if middle.button("Emoji button", icon="😂", use_container_width=True):
    middle.markdown("You clicked the emoji button.")
if right.button("Material button", icon=":material/mood:", use_container_width=True):
    right.markdown("You clicked the Material button.")