def plot_grid_scores(param_name, cv_result, ylim=(0, 1.1)):
    param_values = np.array(cv_result["param_%s" % param_name])

    plt.title("Scores for %s." % param_name)

    plt.ylim(*ylim)
    plt.grid()
    plt.xlim(min(param_values), max(param_values))
    plt.xlabel(param_name)
    plt.ylabel("Score")

    train_scores_mean = cv_result['mean_train_score']
    test_scores_mean = cv_result['mean_test_score']
    plt.scatter(param_values, train_scores_mean, marker='o', color="r",
                label="Training scores")
    plt.scatter(param_values, test_scores_mean, marker='o', color="g",
                label="Cross-validation scores")
    plt.legend(loc="best")
    print("Best test score: {:.4f}".format(test_scores_mean[-1]))


plot_grid_scores("max_depth", grid_search.cv_results_)
