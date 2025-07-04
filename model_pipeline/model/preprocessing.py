from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from config import CAT_COLS, NUM_COLS

def build_preprocessor():
    cat_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("ohe", OneHotEncoder(drop="first", handle_unknown="ignore"))
    ])
    num_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="median"))
    ])

    transformer = ColumnTransformer([
        ("cat", cat_pipe, CAT_COLS),
        ("num", num_pipe, NUM_COLS),
    ])

    return transformer
