[Hack n Lead 2019](https://womenplusplus.ch/hacknlead)

# SCEED: Future focused AML risk model

===

details in model.ipynb

## 1) Risk monitoring model based on targeted controls to filter out the most suspicious accounts

One of our key approaches was to build a total of 13 risk controls based on the dataset provided by CS.

The objective of each of the controls is to focus on the 5% worst hits resulting from the control (this percentage was applied consistently to each control for the purposes of this project, but ideally should be modified to apply different weights to the controls that further could be grouped together), thus freeing resources from having to deal with too many false positives.

We followed a risk-based approached by adding an external dataset, specifically the Corruption Perception Index (CPI) country rank due to the presence of PEP clients.

Integrating this information into our risk categorisation controls allowed us to concentrate on clients with the highest AML/corruption risks.

Below are brief descriptions of each of the 13 dataset controls as well as the SQL query results thereof which illustrate the total number of clients that ranked highest within each risk category.

We made an attempt to create each control in such ways so as to reduce false positives (cf. below control regarding age and excluding Japan) to catch the most relevant suspicious clients/transactions.

#risk parameters:

'rp_turnover_cpi':
 -- 50'000 clients with top 5% highest turnover, thereof:
 -- 12'703 in connection with top 5% highest CPI_rank

'rp_trx_count_cpi'
 -- 50'590 clients with top 5% highest transaction count, thereof:
 -- 12'650 in connection with top 5% highest CPI_rank

'rp_io_ratio_0.5_cpi'
 -- 91'324 clients with io_ratio < 0.5 (inflow > outflows), thereof:
 -- 23'016 in connection with top 5% highest CPI_rank

'rp_io_ratio_1_cpi'
 -- 115'227 clients with io_ratio = 1 (only outflows), thereof:
 -- 29'007 in connection with top 5% highest CPI_rank

'rp_age'
 -- 699'757 clients with age > 0, thereof:
 -- >> 27'915 in top 5% (= high age) and excl. Japan (due to longevity)

'rp_nationality_cpi'
 -- cpi (corruption perception index): 945'468 clients with a CPI_rank, thereof:
 -- >> 19'905 in top 5% highest CPI_rank

'rp_pep_cpi'
 -- total PEPs = 6'851 (%), thereof:
 -- 1'752 fall within top 5% highest CPI_rank

'rp_inactive_min_cpi'
 -- 13'231 clients with top 5% min. inactive days and in connection with top 5% highest CPI_rank

'rp_inactive_avg_cpi'
 -- 12'562 clients with top 5% min. avg. inactive days and in connection with top 5% highest CPI_rank

'rp_accounts'
 -- 630'713 clients with >1 account, thereof:
 -- 80'043 within top 5% (most number of accounts)

'rp_counterparties'
 -- 383'869 clients with [distinct_counterparties] > 1, thereof:
 -- 19'352 within top 5% (most number of distinct counterparties)

'rp_withdrawal_cpi'
 -- 12'617 clients with top 5% highest cash withdrawals amount and in connection with top 5% highest CPI_rank

'rp_deposit_cpi'
 -- 12'680 clients with top 5% highest cash deposits amount and in connection with top 5% highest CPI_rank

1 risk point is given to each client who falls into the top5% of a control
End result:
PowerBI file:
- CS large dataset +risk points for each of the 13 controls (tab "data_riskpara_all")
- table where 1 point was awarded in a risk category (tab "1RiskPt_x13")
- table with max. risk points obtained per client (tab "maxRPs")

>>>>> Data analysis FINAL OUTPUT: 
 10 clients who scored 8 points (max. out of a possible 13; total of 618 clients who scored 7 points) cf. 17'141 accounts on the CS suspect list.
 Applying the most effective and relevant filters helps save valuable ressources that would otherwise be wasted on analysing false positives!

## 2) Exploratory Feature analysis

We started exploratory data analysis by summarising main characteristics of selected features and feature combinations. Our assumption was that distribution pattern of these subsets of data should reveal outliers that will be marked as suspicious accounts. Such analysis revealed only one significant feature combination: category: “individual”, turnover and transaction count which lead to 7 “Red Flags” with 1 false positive.

Significance of this features was further developed in the next part.

## 3) Clustering clients to find outliers 

We attemted to find outstanding characteristics of criminal records. In this part we focused on natural persons only.
Examples of successful analysis are as following:
- Coupling the transaction count with the io_ratio, two distinctive distributions are found where one corresponds to the suspicious clients, and the other to the rest. [image 1].
This results in 500 hits with less than 2% false positive. There is still room for improving the model's precision.  


