import requests
import bs4
import re
import spacy
import os
import logging
from typing import List, Optional, Tuple
import random

import nltk
import string
import numpy as np
import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from heapq import nlargest
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('stopwords')

logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')

def fetch_job_description(url: str, headers: Optional[dict] = None) -> str:
    """
    Fetches and cleans job description text from the given URL.

    Parameters:
    url (str): The URL of the job description page.
    headers (Optional[dict]): Optional headers to include in the request.

    Returns:
    str: Cleaned job description text.
    """
    try:
        # Make the HTTP request
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Parse the HTML content
        soup = bs4.BeautifulSoup(response.content, 'lxml')

        # Extract text from HTML
        job_description = soup.get_text(separator=' ', strip=True)

        # Clean the extracted text
        job_description = job_description.replace(u'\xa0', u' ')
        job_description = job_description.replace(u'\xad', u' ')
        job_description = re.sub(r'\s+', ' ', job_description).strip()

        logging.info(f"Successfully fetched and cleaned job description from {url}")
        return job_description

    except requests.RequestException as e:
        logging.error(f"HTTP request error: {e}")
        return ""
    except Exception as e:
        logging.error(f"An error occurred while processing the job description: {e}")
        return ""


def extract_text_between_keywords(text, start_keyword, end_keyword):
    """
    Extract text between two keywords in a given string.

    Parameters:
    text (str): The unstructured text to search within.
    start_keyword (str): The starting keyword.
    end_keyword (str): The ending keyword.

    Returns:
    str: The extracted text between the two keywords.
    """
    # Regex pattern to extract text between start_keyword and end_keyword
    pattern = re.compile(re.escape(start_keyword) + r'(.*?)' + re.escape(end_keyword), re.DOTALL)

    # Search for the pattern in the text
    match = pattern.search(text)

    # Extract and return the matched text if found
    if match:
        extracted_text = match.group(1).strip()
        extracted_text = re.sub(r'\s+', ' ', extracted_text).strip()
        return extracted_text
    else:
        return "The specified text range was not found."


def extract_number_from_string(url):
    """
    Extract the first number found in a given string.

    :param url: The input string from which to extract the number.
    :return: The extracted number as a string, or None if no number is found.
    """
    matches = re.findall(r'\d+', url)
    if matches:
        return ''.join(matches)
    else:
        return str(random.randint(1000, 999999999))


def save_string_to_txt(directory, filename, content):
    """
    Save a string to a text file in a specified directory.

    :param directory: The directory where the file will be saved.
    :param filename: The name of the file to save the content.
    :param content: The string content to save to the file.
    """
    # Create directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Full path to the file
    filepath = os.path.join(directory, filename + '.txt')

    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Content successfully saved to {filepath}")
    except Exception as e:
        print(f"An error occurred while saving to {filepath}: {e}")


def preprocess_text(text: str) -> Tuple[List[str], List[str]]:
    """
    Tokenizes the text into sentences and words, removing stopwords and punctuation.

    Args:
        text (str): The input text to preprocess.

    Returns:
        Tuple[List[str], List[str]]: A tuple containing the original sentences and the processed sentences.
    """
    try:
        # Tokenize text into sentences
        sentences = sent_tokenize(text)

        # Tokenize sentences into words and remove stopwords and punctuation
        stop_words = set(stopwords.words('english'))
        processed_sentences = []
        for sentence in sentences:
            words = word_tokenize(sentence.lower())
            words = [word for word in words if word not in stop_words and word not in string.punctuation]
            processed_sentences.append(" ".join(words))

        return sentences, processed_sentences
    except Exception as e:
        logging.error(f"Error in preprocessing text: {e}")
        return [], []


def build_similarity_matrix(sentences: List[str]) -> List[List[float]]:
    """
    Builds a similarity matrix using TF-IDF vectors and cosine similarity.

    Args:
        sentences (List[str]): A list of sentences.

    Returns:
        List[List[float]]: A similarity matrix.
    """
    try:
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(sentences)
        similarity_matrix = cosine_similarity(tfidf_matrix)
        return similarity_matrix.tolist()  # Convert to nested list
    except Exception as e:
        logging.error(f"Error in building similarity matrix: {e}")
        return []


def apply_textrank(similarity_matrix: List[List[float]]) -> dict:
    """
    Applies the TextRank algorithm on the similarity matrix to rank sentences.

    Args:
        similarity_matrix (List[List[float]]): A similarity matrix.

    Returns:
        dict: A dictionary of sentence scores.
    """
    try:
        similarity_matrix_np = np.array(similarity_matrix)
        nx_graph = nx.from_numpy_array(similarity_matrix_np)
        scores = nx.pagerank(nx_graph)
        return scores
    except Exception as e:
        logging.error(f"Error in applying TextRank: {e}")
        return {}


def extract_summary(text: str, summary_length: int = 3) -> str:
    """
    Extracts a summary from the text using the TextRank algorithm.

    Args:
        text (str): The input text to summarize.
        summary_length (int): The number of sentences to include in the summary. Default is 3.

    Returns:
        str: The extracted summary.
    """
    try:
        sentences, processed_sentences = preprocess_text(text)
        if not sentences or not processed_sentences:
            return ""

        similarity_matrix = build_similarity_matrix(processed_sentences)
        if not similarity_matrix:
            return ""

        sentence_scores = apply_textrank(similarity_matrix)
        if not sentence_scores:
            return ""

        sentence_score_pairs = [(sentence_scores[i], s) for i, s in enumerate(sentences)]
        top_sentences = nlargest(summary_length, sentence_score_pairs, key=lambda x: x[0])
        summary = " ".join([sentence for score, sentence in top_sentences])
        return summary
    except Exception as e:
        logging.error(f"Error in extracting summary: {e}")
        return ""


def process_job_descriptions(urls: list, start_keyword: str, end_keyword: str,
                             description_directory: str, summary_directory: str,
                             summary_length: int = 3, headers: dict = None):
    """
    Process job descriptions from a list of URLs.

    Args:
        urls (list): List of URLs containing job descriptions.
        start_keyword (str): Start keyword to extract text.
        end_keyword (str): End keyword to extract text.
        description_directory (str): Directory to save extracted descriptions.
        summary_directory (str): Directory to save extracted summaries.
        summary_length (int): The number of sentences to include in the summary. Default is 3.
        headers (dict): Headers to be used for making HTTP requests.
    """
    if headers is None:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.5'
        }

    for url in urls:
        try:
            # Fetch job description
            job_description = fetch_job_description(url, headers)

            # Extract text between start and end keywords
            extracted_text = extract_text_between_keywords(job_description, start_keyword, end_keyword)

            # Extract summary
            summary = extract_summary(extracted_text, summary_length)

            # Save description and summary to files
            filename = extract_number_from_string(url)
            save_string_to_txt(description_directory, filename, extracted_text)
            save_string_to_txt(summary_directory, filename, summary)
        except Exception as e:
            print(f"Error processing job description from URL: {url}")
            print(f"Error message: {str(e)}")


def extract_skills(text: str,
                   use_ru: bool = True,
                   use_en: bool = True,
                   ru_model: str = 'ru_core_news_sm',
                   en_model: str = 'en_core_web_sm',
                   entity_labels: Optional[List[str]] = None) -> List[str]:
    """
    Extracts unique skills from a job description text using specified spaCy models for Russian and English.

    Parameters:
    text (str): The input text containing the job description.
    use_ru (bool): Toggle the use of the Russian model. Default is True.
    use_en (bool): Toggle the use of the English model. Default is True.
    ru_model (str): The spaCy model to use for Russian. Default is 'ru_core_news_sm'.
    en_model (str): The spaCy model to use for English. Default is 'en_core_web_sm'.
    entity_labels (Optional[List[str]]): A list of entity labels to extract. Default is None,
                                         which uses ['ORG', 'GPE', 'PRODUCT', 'PER', 'EVENT', 'PERSON'].

    Returns:
    List[str]: A list of unique skills/entities extracted from the job description.
    """
    if entity_labels is None:
        entity_labels = ['ORG', 'GPE', 'PRODUCT', 'PER', 'EVENT', 'PERSON']

    nlp_ru = spacy.load(ru_model) if use_ru else None
    nlp_en = spacy.load(en_model) if use_en else None

    def has_cyrillic(text):
        """Check if the text contains Cyrillic characters."""
        return bool(re.search('[\u0400-\u04FF]', text))

    def clean_skill(skill):
        """Remove leading and trailing spaces and split on various separators."""
        return [s.strip() for s in re.split(r'[,/;+\-]', skill) if s.strip()]

    def extract_entities(doc, entity_labels):
        """Extract entities from the spaCy document based on the specified labels and clean them."""
        entities = set()
        for ent in doc.ents:
            if ent.label_ in entity_labels and not has_cyrillic(ent.text):
                entities.update(clean_skill(ent.text))
        return entities

    entities = set()

    if use_ru and nlp_ru:
        doc_ru = nlp_ru(text)
        entities.update(extract_entities(doc_ru, entity_labels))

    if use_en and nlp_en:
        doc_en = nlp_en(text)
        entities.update(extract_entities(doc_en, entity_labels))

    return list(entities)


def extract_skills_from_files(directory: str, 
                            entity_labels: Optional[List[str]] = None):
    """
    Extracts skills from each text file in the given directory.

    Args:
        directory (str): The directory containing the text files.
        extract_skills_function (function): The function to extract skills from a string.

    Returns:
        list: A list of extracted skills.
    """
    all_skills = []

    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        # Check if the file is a text file
        if filename.endswith(".txt"):
            try:
                # Open the file and read its content
                with open(filepath, 'r', encoding='utf-8') as file:
                    text = file.read()
                
                # Extract skills from the text using the provided function
                skills = extract_skills(text = text, entity_labels = entity_labels)
                
                # Add the extracted skills to the common list
                all_skills.extend(skills)
            except Exception as e:
                print(f"An error occurred while processing {filepath}: {e}")
    
    return all_skills


def concatenate_text_files(directory):
    """
    Concatenates the content of all text files in the given directory into a single string.

    Args:
        directory (str): The directory containing the text files.

    Returns:
        str: The concatenated content of all text files.
    """
    concatenated_text = ""

    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        # Check if the file is a text file
        if filename.endswith(".txt"):
            try:
                # Open the file and read its content
                with open(filepath, 'r', encoding='utf-8') as file:
                    text = file.read()
                
                # Add space before appending text if the concatenated_text is not empty
                if concatenated_text:
                    concatenated_text += " "
                
                # Append the content of the file to the common string
                concatenated_text += text
            except Exception as e:
                print(f"An error occurred while processing {filepath}: {e}")
    
    return concatenated_text
