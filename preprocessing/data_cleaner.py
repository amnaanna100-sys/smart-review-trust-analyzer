"""
Advanced data cleaning utilities for review text
"""

import re
import string
import unicodedata
from typing import List, Tuple


class DataCleaner:
    """Advanced text data cleaning"""
    
    @staticmethod
    def remove_html_tags(text: str) -> str:
        """
        Remove HTML tags from text
        
        Args:
            text: Text containing HTML
            
        Returns:
            Cleaned text
        """
        pattern = r'<[^>]+>'
        return re.sub(pattern, '', text)
    
    @staticmethod
    def remove_urls(text: str) -> str:
        """
        Remove URLs from text
        
        Args:
            text: Text containing URLs
            
        Returns:
            Text without URLs
        """
        pattern = r'http\S+|www\S+|https\S+'
        return re.sub(pattern, '', text)
    
    @staticmethod
    def remove_emails(text: str) -> str:
        """
        Remove email addresses
        
        Args:
            text: Text containing emails
            
        Returns:
            Text without emails
        """
        pattern = r'\S+@\S+'
        return re.sub(pattern, '', text)
    
    @staticmethod
    def remove_phone_numbers(text: str) -> str:
        """
        Remove phone numbers
        
        Args:
            text: Text containing phone numbers
            
        Returns:
            Text without phone numbers
        """
        pattern = r'\+?1?\d{9,15}'
        return re.sub(pattern, '', text)
    
    @staticmethod
    def normalize_whitespace(text: str) -> str:
        """
        Normalize whitespace
        
        Args:
            text: Text with irregular whitespace
            
        Returns:
            Text with normalized whitespace
        """
        # Replace multiple spaces with single space
        text = re.sub(r'\s+', ' ', text)
        # Remove leading/trailing whitespace
        return text.strip()
    
    @staticmethod
    def remove_special_characters(text: str, keep_punctuation: bool = False) -> str:
        """
        Remove special characters
        
        Args:
            text: Text containing special characters
            keep_punctuation: Keep punctuation marks
            
        Returns:
            Cleaned text
        """
        if keep_punctuation:
            pattern = r'[^a-zA-Z0-9\s.!?-]'
        else:
            pattern = r'[^a-zA-Z0-9\s]'
        return re.sub(pattern, '', text)
    
    @staticmethod
    def remove_accents(text: str) -> str:
        """
        Remove accents from characters
        
        Args:
            text: Text with accents
            
        Returns:
            Text without accents
        """
        nfkd_form = unicodedata.normalize('NFKD', text)
        return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])
    
    @staticmethod
    def expand_contractions(text: str) -> str:
        """
        Expand English contractions
        
        Args:
            text: Text with contractions
            
        Returns:
            Text with expanded contractions
        """
        contractions_dict = {
            "ain't": "am not",
            "aren't": "are not",
            "can't": "cannot",
            "can't've": "cannot have",
            "could've": "could have",
            "didn't": "did not",
            "doesn't": "does not",
            "don't": "do not",
            "hadn't": "had not",
            "hasn't": "has not",
            "haven't": "have not",
            "he'd": "he would",
            "he'll": "he will",
            "he's": "he is",
            "how'd": "how did",
            "how'll": "how will",
            "how's": "how is",
            "i'd": "i would",
            "i'll": "i will",
            "i'm": "i am",
            "i've": "i have",
            "isn't": "is not",
            "it'd": "it would",
            "it'll": "it will",
            "it's": "it is",
            "let's": "let us",
            "shouldn't": "should not",
            "that's": "that is",
            "there's": "there is",
            "they'd": "they would",
            "they'll": "they will",
            "they're": "they are",
            "they've": "they have",
            "wasn't": "was not",
            "we'd": "we would",
            "we'll": "we will",
            "we're": "we are",
            "we've": "we have",
            "weren't": "were not",
            "what's": "what is",
            "who'd": "who would",
            "who'll": "who will",
            "who're": "who are",
            "who's": "who is",
            "won't": "will not",
            "wouldn't": "would not",
            "you'd": "you would",
            "you'll": "you will",
            "you're": "you are",
            "you've": "you have"
        }
        
        pattern = re.compile(r'\b(' + '|'.join(contractions_dict.keys()) + r')\b')
        return pattern.sub(lambda m: contractions_dict[m.group(0).lower()], text.lower())
    
    @staticmethod
    def remove_duplicate_chars(text: str, threshold: int = 2) -> str:
        """
        Remove duplicate characters
        
        Args:
            text: Text with duplicate characters
            threshold: Number of duplicates to allow
            
        Returns:
            Text with reduced duplicates
        """
        pattern = r'(.)\1{' + str(threshold - 1) + r',}'
        return re.sub(pattern, r'\1' * threshold, text)
    
    @staticmethod
    def full_clean(text: str) -> str:
        """
        Comprehensive text cleaning pipeline
        
        Args:
            text: Raw text
            
        Returns:
            Fully cleaned text
        """
        if not isinstance(text, str):
            return ""
        
        # Remove HTML tags
        text = DataCleaner.remove_html_tags(text)
        
        # Remove URLs
        text = DataCleaner.remove_urls(text)
        
        # Remove emails
        text = DataCleaner.remove_emails(text)
        
        # Remove phone numbers
        text = DataCleaner.remove_phone_numbers(text)
        
        # Expand contractions
        text = DataCleaner.expand_contractions(text)
        
        # Remove accents
        text = DataCleaner.remove_accents(text)
        
        # Convert to lowercase
        text = text.lower()
        
        # Remove duplicate characters
        text = DataCleaner.remove_duplicate_chars(text)
        
        # Remove special characters
        text = DataCleaner.remove_special_characters(text)
        
        # Normalize whitespace
        text = DataCleaner.normalize_whitespace(text)
        
        return text
