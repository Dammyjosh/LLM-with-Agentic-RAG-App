# import streamlit as st
# from fetcher import fetch_articles
# from summarizer import summarize_text
# from report_generator import generate_markdown_report, convert_md_to_pdf

# st.set_page_config(page_title="InsightReporter", layout="centered")

# st.title("🧠 InsightReporter")
# st.markdown("Get instant insights on any topic using real-time search and AI summarization.")

# query = st.text_input("Enter a topic to research:", value="Latest AI news")

# if st.button("🔍 Generate Report"):
#     with st.spinner("Fetching articles..."):
#         articles = fetch_articles(query)

#     if not articles:
#         st.error("No articles found.")
#     else:
#         with st.spinner("Summarizing content..."):
#             summaries = []
#             for article in articles:
#                 content = article.get("content", "")[:1500]
#                 if content:
#                     summary = summarize_text(content)
#                     summaries.append({
#                         "title": article["title"],
#                         "url": article["url"],
#                         "summary": summary
#                     })

#         with st.spinner("Generating markdown and PDF reports..."):
#             md_file = generate_markdown_report(summaries)
#             pdf_file = convert_md_to_pdf(md_file)

#         st.success("✅ Report generated!")
#         st.subheader("📝 Report Preview")
#         with open(md_file, "r", encoding="utf-8") as f:
#             st.markdown(f.read())

#         col1, col2 = st.columns(2)
#         with col1:
#             with open(md_file, "rb") as f:
#                 st.download_button("📄 Download Markdown", f, file_name="report.md")

#         with col2:
#             with open(pdf_file, "rb") as f:
#                 st.download_button("📄 Download PDF", f, file_name="report.pdf")

                


import streamlit as st
from fetcher import fetch_articles
from summarizer import summarize_text
from report_generator import generate_markdown_report, convert_md_to_pdf

st.set_page_config(page_title="InsightReporter", layout="centered")

st.title("InsightReporter")
st.markdown("Get instant insights on any topic using real-time search and AI summarization.")

query = st.text_input("Enter a topic to research:", value="Latest AI news")

if st.button("🔍 Generate Report"):
    with st.spinner("Fetching articles..."):
        articles = fetch_articles(query)

    if not articles:
        st.error("No articles found.")
    else:
        with st.spinner("Summarizing content..."):
            summaries = []
            for article in articles:
                content = article.get("content", "")[:1500]
                if content:
                    summary = summarize_text(content)
                    summaries.append({
                        "title": article["title"],
                        "url": article["url"],
                        "summary": summary
                    })

        st.success("✅ Summaries Ready!")
        st.subheader("📚 Article Summaries")
        for i, item in enumerate(summaries, 1):
            st.markdown(f"### {i}. {item['title']}")
            st.markdown(f"**URL**: {item['url']}")
            st.markdown(f"**Summary**: {item['summary']}")
            st.markdown("---")

        with st.spinner("Generating markdown and PDF reports..."):
            md_file = generate_markdown_report(summaries)
            pdf_file = convert_md_to_pdf(md_file)

        st.success("📄 Report generated!")
        col1, col2 = st.columns(2)
        with col1:
            with open(md_file, "rb") as f:
                st.download_button("📥 Download Markdown", f, file_name="report.md")

        with col2:
            with open(pdf_file, "rb") as f:
                st.download_button("📥 Download PDF", f, file_name="report.pdf")






