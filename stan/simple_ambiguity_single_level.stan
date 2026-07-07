// Single-level ambiguity-value model.
//
// This model is the first non-GLM milestone toward the final hierarchical
// Bayesian model suite. It is intended for synthetic-data recovery checks before
// any confidential RAID data are used.

data {
  int<lower=1> N;
  array[N] int<lower=0, upper=1> choice;
  vector<lower=0, upper=1>[N] probability;
  vector<lower=0, upper=1>[N] ambiguity;
  vector<lower=0>[N] value;
  vector[N] ref_side;
}

parameters {
  real alpha;
  real<lower=0> beta_ambiguity;
  real<lower=0> tau;
  real side_bias;
}

transformed parameters {
  vector[N] subjective_value;
  subjective_value = value .* (probability - beta_ambiguity * ambiguity / 2);
}

model {
  alpha ~ normal(0, 2);
  beta_ambiguity ~ normal(0.75, 0.75);
  tau ~ lognormal(log(4), 0.75);
  side_bias ~ normal(0, 0.5);

  choice ~ bernoulli_logit(alpha + tau * subjective_value + side_bias * ref_side);
}

generated quantities {
  vector[N] log_lik;
  array[N] int y_rep;

  for (n in 1:N) {
    real eta_n = alpha + tau * subjective_value[n] + side_bias * ref_side[n];
    log_lik[n] = bernoulli_logit_lpmf(choice[n] | eta_n);
    y_rep[n] = bernoulli_logit_rng(eta_n);
  }
}
