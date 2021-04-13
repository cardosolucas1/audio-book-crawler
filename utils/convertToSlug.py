import re
from unicodedata import normalize


def remover_acentos(string):
    return normalize('NFKD', string).encode('ASCII', 'ignore').decode('ASCII')


def convertToSlug(string):
  prepare = remover_acentos(string).lower()
  return re.sub(r'[\W_]+', '-', prepare)
