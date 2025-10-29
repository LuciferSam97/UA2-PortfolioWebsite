import streamlit as st

st.title("Documents")
st.divider()

st.markdown("Here you can find pdfs of various relevant documents. Currently, I've only uploaded my CV, "
            "the dissertation I wrote as part of my integrated masters at Durham, and some of my certificates. "
            "More may be added in the future!")
st.header("CV")
st.markdown("My curriculum vitae as of October 2025")

st.pdf(data="static/documents/CV.pdf",
       height=600)

with open("static/documents/CV.pdf", "rb") as file:
    st.download_button(label=":material/download: Download PDF", data=file,
                       file_name="sam_richards_CV", mime="application/pdf", key="CV_pdf")

st.divider()

st.header("Masters Dissertation")
st.markdown("This is a dissertation on symmetry and supersymmetry with a distinctly geometrical flavour. "
            "I've also included the academic poster I created as part of the project. I am aware of some errors in both"
            "of these and hope to find some time to address these in the future.")

diss_cols = st.columns(2)

with diss_cols[0].container(width=600):
    st.subheader("Written Report")
    st.pdf(data="static/documents/SUSY_Dissertation.pdf",
           height=600)
    with open("static/documents/SUSY_Dissertation.pdf", "rb") as file:
        st.download_button(label=":material/download: Download PDF", data=file,
                           file_name="sam_richards_SUSY_dissertation", mime="application/pdf", key="Diss_pdf")

with diss_cols[1].container(width=600):
    st.subheader("Poster")
    st.image(image="static/documents/Superspace_Poster.jpg",)
    with open("static/documents/Superspace_Poster.pdf", "rb") as file:
        st.download_button(label=":material/download: Download PDF", data=file,
                           file_name="sam_richards_SUSY_poster", mime="application/pdf", key="Poster_pdf")

st.divider()

st.header("Certificates")

cert_cols = st.columns(2)

with cert_cols[0].container(width=600):
    st.subheader("Certificate from the University of Durham")
    st.image(image="static/documents/Durham_cert.jpg", use_container_width=True)

with cert_cols[1].container(width=600):
    st.subheader("Certificate from the University of Cambridge")
    st.image(image="static/documents/Cambridge_cert.jpg", use_container_width=True)
