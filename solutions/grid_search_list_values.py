print("max_depth, train_score, test_score")
for n, max_depth in enumerate(grid_search.cv_results_['param_max_depth']):
    print(max_depth,
          grid_search.cv_results_['mean_train_score'][n],
          grid_search.cv_results_['mean_test_score'][n],)
