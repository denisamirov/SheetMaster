# SheetMaster
**Google Sheets** — is a powerful tool for organizing, analyzing and sharing data, which is ideal for teamwork of programmers. Our project helps to quickly create Google tables and enter data into them.

[source](https://github.com/denisamirov/SheetMaster)

### Team
- [Sofia](https://github.com/Sofia-Fadeeva) - developer
- [Arslan](https://github.com/ARSLAN20128) - analyst
- [Aliya](https://github.com/pypsik007) - tester
- [Ranel](https://github.com/ranel211) - developer

### [Dependencies used](./requirements.txt)

### Launch conditions

### Style

| Prefix   | Description                                  |
|------------|----------------------------------------------|
| `feat`     | Adds a new feature                           |
| `fix`      | Fixes a bug                                  |
| `refactor` | Code improvement (no feature change)        |
| `test`     | Adds tests                                   |
| `style`    | Formatting (affects looks, not code logic) |
| `ci`       | CI/CD pipeline changes                       |
| `docs`     | Updates documentation                        |
| `chore`   | Build process or auxiliary tool changes     |

#### Commits

| Rule         | Example      |
|--------------|--------------|
| prefix: #number | feat: #9     |

#### Branches

| Rule         | Example      |
|--------------|--------------|
| prefix-number task | feat-9   |

### Fast steps

#### Start API
```
uvicorn main:app --reload
```

#### Install lib
```
python -m pip install -r requirements.txt
```

#### Pylint
```
pylint main.py
```