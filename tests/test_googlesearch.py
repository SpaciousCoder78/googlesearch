# Introduced unit tests with pytest to make the development process a bit easier
import webbrowser
from googlesearch import *
import pytest

#sample test query
ser = "test query"

@pytest.fixture
def search_query():
	return "test query"

# opening the web browser to test the library since using simple `search("google")` does not work
def test_searchactual(search_query):
	search(search_query)
	webbrowser.open_new_tab(next(search(search_query)))
	return True
	
#using pytest to check if the test passes
def test_search():
	assert search(ser) is not None