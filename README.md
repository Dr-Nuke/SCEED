# [Hack n Lead 2019](https://womenplusplus.ch/hacknlead)

===

## Steps

1. `Fork` this repository
2. Add your team members as contributors
3. Put your presentation in the `docs/` folder
4. This repository **must** be open source (and licensed) in order to submit



--rp = risk parameter
    
    -- 50'000 clients with top 5% highest turnover, thereof:
    -- 12'703 in connection with top 5% highest CPI_rank
    'rp_turnover_cpi'= CASE WHEN PERCENT_RANK() OVER (ORDER BY [transaction_count] desc) <= 0.05 AND cpi.[Rank] BETWEEN 89 AND 189 THEN 1 ELSE 0 END
    -- 50'590 clients with top 5% highest transaction count, thereof:
    -- 12'650 in connection with top 5% highest CPI_rank
    ,'rp_trx_count_cpi'= CASE WHEN PERCENT_RANK() OVER (ORDER BY [turnover] desc) <= 0.05 AND cpi.[Rank] BETWEEN 89 AND 189 THEN 1 ELSE 0 END
    -- 91'324 clients with io_ratio < 0.5 (inflow > outflows), thereof:
    -- 23'016 in connection with top 5% highest CPI_rank
    ,'rp_io_ratio_0.5_cpi'= CASE WHEN [io_ratio] = 0.5 AND cpi.[Rank] BETWEEN 89 AND 189 THEN 1 ELSE 0 END
    -- 115'227 clients with io_ratio = 1 (only outflows), thereof:
    -- 29'007 in connection with top 5% highest CPI_rank
    ,'rp_io_ratio_1_cpi'= CASE WHEN [io_ratio] = 1 AND cpi.[Rank] BETWEEN 89 AND 189 THEN 1 ELSE 0 END
    -- 699'757 clients with age > 0, thereof:
    -- >> 27'915 in top 5% (= high age) and excl. Japan (due to longevity)
    ,'rp_age'= CASE WHEN PERCENT_RANK() OVER (ORDER BY [age] desc) <= 0.05 AND cpi.[Country] <> 'Japan' THEN 1 ELSE 0 END
    -- cpi (corruption perception index): 945'468 clients with a CPI_rank, thereof:
    -- >> 19'905 in top 5% highest CPI_rank
    ,'rp_nationality_cpi'= CASE WHEN cpi.[Rank] BETWEEN 89 AND 189 THEN 1 ELSE 0 END
    -- total PEPs = 6'851 (%), thereof:
    -- 1'752 fall within top 5% highest CPI_rank
    ,'rp_pep_cpi'= CASE WHEN [is_pep] = 1 AND cpi.[Rank] BETWEEN 89 AND 189 THEN 1 ELSE 0 END
    -- 13'231 clients with top 5% min. inactive days and in connection with top 5% highest CPI_rank
    ,'rp_inactive_min_cpi'= CASE WHEN PERCENT_RANK() OVER (ORDER BY [inactive_days_max]) <= 0.05 AND cpi.[Rank] BETWEEN 89 AND 189 THEN 1 ELSE 0 END
    -- 12'562 clients with top 5% min. avg. inactive days and in connection with top 5% highest CPI_rank
    ,'rp_inactive_avg_cpi'= CASE WHEN PERCENT_RANK() OVER (ORDER BY [inactive_days_average]) <= 0.05 AND cpi.[Rank] BETWEEN 89 AND 189 THEN 1 ELSE 0 END
    -- 630'713 clients with >1 account, thereof:
    -- 80'043 within top 5% (most number of accounts)
    ,'rp_accounts'= CASE WHEN [n_of_accounts] > 1 AND PERCENT_RANK() OVER (ORDER BY [n_of_accounts] desc) <= 0.5 THEN 1 ELSE 0 END
    -- 383'869 clients with [distinct_counterparties] > 1, thereof:
    -- 19'352 within top 5% (most number of distinct counterparties)
    ,'rp_counterparties'= CASE WHEN [distinct_counterparties] > 1 AND PERCENT_RANK() OVER (ORDER BY [distinct_counterparties] desc) <= 0.05 THEN 1 ELSE 0 END
    -- 12'617 clients with top 5% highest cash withdrawals amount and in connection with top 5% highest CPI_rank
    ,'rp_withdrawal_cpi'= CASE WHEN PERCENT_RANK() OVER (ORDER BY [atm_withdrawal] DESC) <= 0.5 AND cpi.[Rank] BETWEEN 89 AND 189 THEN 1 ELSE 0 END
    -- 12'680 clients with top 5% highest cash deposits amount and in connection with top 5% highest CPI_rank
    ,'rp_deposit_cpi'= CASE WHEN PERCENT_RANK() OVER (ORDER BY [atm_deposit] DESC) <= 0.5 AND cpi.[Rank] BETWEEN 89 AND 189 THEN 1 ELSE 0 END


