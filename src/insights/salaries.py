from typing import Union, List, Dict
from .jobs import read


def get_max_salary(path: str) -> int:
    # """Get the maximum salary of all jobs

    # Must call `read`

    # Parameters
    # ----------
    # path : str
    #     Must be passed to `read`

    # Returns
    # -------
    # int
    #     The maximum salary paid out of all job opportunities
    # """
    # raise NotImplementedError
    list = read(path)
    max = 0
    salaries = set()
    for item in list:
        if item['max_salary'].isnumeric():
            salaries.add(item['max_salary'])
    for salary in salaries:
        num = int(salary)
        if max < num:
            max = num
    return max
    # return salaries


def get_min_salary(path: str) -> int:
    # """Get the minimum salary of all jobs

    # Must call `read`

    # Parameters
    # ----------
    # path : str
    #     Must be passed to `read`

    # Returns
    # -------
    # int
    #     The minimum salary paid out of all job opportunities
    # """
    # raise NotImplementedError
    list = read(path)
    min = get_max_salary(path)
    salaries = set()
    for item in list:
        if item['min_salary'].isnumeric():
            salaries.add(item['min_salary'])
    for salary in salaries:
        num = int(salary)
        if min > num:
            min = num
    return min


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    # """Checks if a given salary is in the salary range of a given job

    # Parameters
    # ----------
    # job : dict
    #     The job with `min_salary` and `max_salary` keys
    # salary : int
    #     The salary to check if matches with salary range of the job

    # Returns
    # -------
    # bool
    #     True if the salary is in the salary range of the job, False otherwise

    # Raises
    # ------
    # ValueError
    #     If `job["min_salary"]` or `job["max_salary"]` doesn't exists
    #     If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
    #     If `job["min_salary"]` is greather than `job["max_salary"]`
    #     If `salary` isn't a valid integer
    # """
    # raise NotImplementedError
    if(
        "max_salary" not in job or "min_salary" not in job
        or str(job["max_salary"]).isnumeric() is False
        or str(job["min_salary"]).isnumeric() is False
        or int(str(job["min_salary"])) > int(str(job["max_salary"]))
        or str(salary).replace('-', '').isnumeric() is False
      ):
        raise ValueError()

    return int(str(job["min_salary"])) <= int(str(salary)) \
        <= int(str(job["max_salary"]))


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    # """Filters a list of jobs by salary range

    # Parameters
    # ----------
    # jobs : list
    #     The jobs to be filtered
    # salary : int
    #     The salary to be used as filter

    # Returns
    # -------
    # list
    #     Jobs whose salary range contains `salary`
    # """
    # raise NotImplementedError
    list = []
    for job in jobs:
        try:
            boolean = matches_salary_range(job, salary)
            if boolean is True:
                list.append(job)
        except ValueError:
            list = list

    return list
