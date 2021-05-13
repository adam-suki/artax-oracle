# Oracle

This is an a POC for a complementary tool used by [ARTAX](http://outlyingdo.com/tag/artax/).

The goal is to investigate the usability of generated lyrics used for sourcing algorithmic music concepts. 

# Environment
Client access token generated via https://genius.com/api-clients and kept in a plain textfile called ´genius.txt´

Model training should be performed in Colab notebooks with GPU. 


# Dev log
- Scraper implemented using Genius API to pull all lyrics by artist
- Basic data cleaning
- Model building pipeline implemented
- Generation and note mapping tested with wovels and phonetics

# Ideas
- Forther data cleaning options (repetitions, etc. )
- Investigate lyrics filtering before moving to corpus based on [semantic classification, Flesch Kincaid Readability Test score, ]
- Incorporating TL Models, and Style match architecture


# References
- [Generating Poetry using Neural Networks](https://neuro.cs.ut.ee/wp-content/uploads/2018/02/poetry.pdf)
- [https://medium.com/@DenisKrivitski/generation-of-poems-with-a-recurrent-neural-network-128a5f62b483](https://medium.com/@DenisKrivitski/generation-of-poems-with-a-recurrent-neural-network-128a5f62b483)
- [Scraper](https://chrishyland.github.io/scraping-from-genius/)
- [Flesch Kincaid Readability Tests](https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests)
- [google-research-datasets/poem-sentiment](https://github.com/google-research-datasets/poem-sentiment)
- [Google Research - Semantic Experiences](https://research.google.com/semanticexperiences/for-developers.html)
- [universal-sentence-encoder](https://tfhub.dev/google/universal-sentence-encoder/1)