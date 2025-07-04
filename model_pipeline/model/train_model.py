from sklearn.model_selection import train_test_split, RepeatedKFold
from config import CAT_COLS, NUM_COLS, TARGET, TEST_SIZE, RAND_STATE
from model_utils import build_ridge_pipeline, evaluate, save_model, get_artifact_dir
from data_loader import load_data

def main():
    df = load_data()
    X = df[CAT_COLS + NUM_COLS]
    y = df[TARGET]

    # Split data for evaluation
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RAND_STATE
    )

    # Pipeline + CV Ridge
    rkf  = RepeatedKFold(n_splits=10, n_repeats=3, random_state=RAND_STATE)
    pipe = build_ridge_pipeline(cv=rkf)

    metrics = evaluate(pipe, X_train, X_test, y_train, y_test, rkf)
    
    artifact_dir = get_artifact_dir()
    save_model(pipe, artifact_dir / "model.joblib")

    print("Training completed")
    print(metrics)

if __name__ == "__main__":
    main()