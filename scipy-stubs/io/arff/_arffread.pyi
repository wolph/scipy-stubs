from scipy._typing import Untyped

r_meta: Untyped
r_comment: Untyped
r_empty: Untyped
r_headerline: Untyped
r_datameta: Untyped
r_relation: Untyped
r_attribute: Untyped
r_nominal: Untyped
r_date: Untyped
r_comattrval: Untyped
r_wcomattrval: Untyped

class ArffError(OSError): ...
class ParseArffError(ArffError): ...

class Attribute:
    type_name: Untyped
    name: Untyped
    range: Untyped
    dtype: Untyped
    def __init__(self, name) -> None: ...
    @classmethod
    def parse_attribute(cls, name, attr_string): ...
    def parse_data(self, data_str): ...

class NominalAttribute(Attribute):
    type_name: str
    values: Untyped
    range: Untyped
    dtype: Untyped
    def __init__(self, name, values) -> None: ...
    @classmethod
    def parse_attribute(cls, name, attr_string) -> Untyped: ...
    def parse_data(self, data_str) -> Untyped: ...

class NumericAttribute(Attribute):
    type_name: str
    dtype: Untyped
    def __init__(self, name) -> None: ...
    @classmethod
    def parse_attribute(cls, name, attr_string) -> Untyped: ...
    def parse_data(self, data_str) -> Untyped: ...

class StringAttribute(Attribute):
    type_name: str
    def __init__(self, name) -> None: ...
    @classmethod
    def parse_attribute(cls, name, attr_string) -> Untyped: ...

class DateAttribute(Attribute):
    date_format: Untyped
    datetime_unit: Untyped
    type_name: str
    range: Untyped
    dtype: Untyped
    def __init__(self, name, date_format, datetime_unit) -> None: ...
    @classmethod
    def parse_attribute(cls, name, attr_string) -> Untyped: ...
    def parse_data(self, data_str) -> Untyped: ...

class RelationalAttribute(Attribute):
    type_name: str
    dtype: Untyped
    attributes: Untyped
    dialect: Untyped
    def __init__(self, name) -> None: ...
    @classmethod
    def parse_attribute(cls, name, attr_string) -> Untyped: ...
    def parse_data(self, data_str) -> Untyped: ...

def to_attribute(name, attr_string) -> Untyped: ...
def csv_sniffer_has_bug_last_field() -> Untyped: ...
def workaround_csv_sniffer_bug_last_field(sniff_line, dialect, delimiters): ...
def split_data_line(line, dialect: Untyped | None = None) -> Untyped: ...
def tokenize_attribute(iterable, attribute) -> Untyped: ...
def tokenize_single_comma(val) -> Untyped: ...
def tokenize_single_wcomma(val) -> Untyped: ...
def read_relational_attribute(ofile, relational_attribute, i) -> Untyped: ...
def read_header(ofile) -> Untyped: ...

class MetaData:
    name: Untyped
    def __init__(self, rel, attr) -> None: ...
    def __iter__(self) -> Untyped: ...
    def __getitem__(self, key) -> Untyped: ...
    def names(self) -> Untyped: ...
    def types(self) -> Untyped: ...

def loadarff(f) -> Untyped: ...
def basic_stats(data) -> Untyped: ...
def print_attribute(name, tp, data): ...
def test_weka(filename): ...
