# Casing Styles Comparison Chart

## Side-by-Side Comparison

Testing with: "Large Language Models and High Agency User Interactions"

```
┌─────────────┬────────────────────────────────────────────────────────┐
│ Style       │ Result                                                 │
├─────────────┼────────────────────────────────────────────────────────┤
│ snake_case  │ large_language_models_and_high_agency_user_interactions│
│ kebab-case  │ large-language-models-and-high-agency-user-interactions│
│ camelCase   │ largeLanguageModelsAndHighAgencyUserInteractions       │
│ PascalCase  │ LargeLanguageModelsAndHighAgencyUserInteractions       │
│ lowercase   │ large language models and high agency user interactions│
│ Title Case  │ Large Language Models And High Agency User Interactions│
└─────────────┴────────────────────────────────────────────────────────┘
```

## Character Count Comparison

| Style | Characters | Readability | File System Safe | URL Safe |
|-------|-----------|-------------|------------------|----------|
| snake_case | 55 | ⭐⭐⭐⭐ | ✅ | ✅ |
| kebab-case | 55 | ⭐⭐⭐⭐ | ✅ | ✅ |
| camelCase | 48 | ⭐⭐⭐ | ✅ | ✅ |
| PascalCase | 48 | ⭐⭐⭐ | ✅ | ✅ |
| lowercase | 55 | ⭐⭐⭐⭐⭐ | ⚠️ | ❌ |
| Title Case | 55 | ⭐⭐⭐⭐⭐ | ⚠️ | ❌ |

## Pros & Cons

### snake_case
✅ Python standard  
✅ Very readable  
✅ Terminal-friendly  
✅ Cross-platform safe  
❌ Slightly longer  

### kebab-case
✅ URL-friendly  
✅ Modern/clean look  
✅ Git-friendly  
✅ Web standard  
❌ Can't use in some programming contexts  

### camelCase
✅ Compact  
✅ JavaScript standard  
✅ No separators  
❌ Harder to read long names  
❌ Less scannable  

### PascalCase
✅ Compact  
✅ Professional  
✅ Class/component standard  
❌ Harder to read long names  
❌ Less scannable  

### lowercase
✅ Most readable  
✅ Natural language  
✅ User-friendly  
❌ Spaces cause issues in terminals  
❌ Not URL-safe  
❌ Requires quoting  

### Title Case
✅ Very professional  
✅ Perfect readability  
✅ Formal documents  
❌ Spaces cause issues in terminals  
❌ Not URL-safe  
❌ Requires quoting  

## Real-World File Comparisons

### Academic Paper
```
Original: paper-draft-final-v3.pdf

snake_case:  deep_learning_for_medical_image_analysis.pdf
kebab-case:  deep-learning-for-medical-image-analysis.pdf
camelCase:   deepLearningForMedicalImageAnalysis.pdf
PascalCase:  DeepLearningForMedicalImageAnalysis.pdf
lowercase:   deep learning for medical image analysis.pdf
Title Case:  Deep Learning For Medical Image Analysis.pdf
```

### Python Script
```
Original: script123.py

snake_case:  data_analysis_with_pandas_numpy.py         ⭐ BEST
kebab-case:  data-analysis-with-pandas-numpy.py
camelCase:   dataAnalysisWithPandasNumpy.py
PascalCase:  DataAnalysisWithPandasNumpy.py
lowercase:   data analysis with pandas numpy.py
Title Case:  Data Analysis With Pandas Numpy.py
```

### React Component
```
Original: component1.jsx

snake_case:  user_profile_card_component.jsx
kebab-case:  user-profile-card-component.jsx
camelCase:   userProfileCardComponent.jsx
PascalCase:  UserProfileCardComponent.jsx                ⭐ BEST
lowercase:   user profile card component.jsx
Title Case:  User Profile Card Component.jsx
```

### Web Image
```
Original: IMG_1234.jpg

snake_case:  beautiful_sunset_over_mountain_lake.jpg
kebab-case:  beautiful-sunset-over-mountain-lake.jpg    ⭐ BEST
camelCase:   beautifulSunsetOverMountainLake.jpg
PascalCase:  BeautifulSunsetOverMountainLake.jpg
lowercase:   beautiful sunset over mountain lake.jpg
Title Case:  Beautiful Sunset Over Mountain Lake.jpg
```

### Word Document
```
Original: research-doc-v2.docx

snake_case:  large_language_models_user_study.docx
kebab-case:  large-language-models-user-study.docx
camelCase:   largeLanguageModelsUserStudy.docx
PascalCase:  LargeLanguageModelsUserStudy.docx
lowercase:   large language models user study.docx
Title Case:  Large Language Models User Study.docx      ⭐ BEST
```

## Compatibility Matrix

| Style | Unix/Linux | macOS | Windows | Git | URLs | Python | JavaScript |
|-------|-----------|-------|---------|-----|------|--------|------------|
| snake_case | ✅ | ✅ | ✅ | ✅ | ✅ | ⭐ | ✅ |
| kebab-case | ✅ | ✅ | ✅ | ✅ | ⭐ | ✅ | ✅ |
| camelCase | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⭐ |
| PascalCase | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⭐ |
| lowercase | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ❌ | ❌ | ❌ |
| Title Case | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ❌ | ❌ | ❌ |

⭐ = Best choice for this context  
✅ = Fully compatible  
⚠️ = Works but may need quoting  
❌ = Not recommended  

## Industry Standards

### Programming Languages
- **Python**: snake_case
- **JavaScript**: camelCase
- **Java**: PascalCase (classes), camelCase (methods)
- **C++**: snake_case or PascalCase
- **Go**: PascalCase (exported), camelCase (unexported)
- **Rust**: snake_case

### File Types
- **Python files (.py)**: snake_case
- **JavaScript files (.js)**: camelCase
- **React components (.jsx)**: PascalCase
- **CSS files (.css)**: kebab-case
- **Images (web)**: kebab-case
- **Documents (.pdf, .docx)**: Title Case or kebab-case

## Command Examples

```bash
# Match your project's style
python rename_files.py ~/Code/python-project/ --case snake --execute
python rename_files.py ~/Code/react-app/src/ --case pascal --execute
python rename_files.py ~/Documents/papers/ --case title --execute
python rename_files.py ~/Website/images/ --case kebab --execute

# Preview different styles before choosing
python rename_files.py data/ --case snake
python rename_files.py data/ --case kebab  
python rename_files.py data/ --case title
# Then execute your favorite
python rename_files.py data/ --case kebab --execute
```

## Recommendations by Use Case

| Use Case | Recommended | Reason |
|----------|------------|--------|
| Python project | snake_case | Language convention |
| React/Vue project | PascalCase | Component standard |
| Web assets | kebab-case | URL/SEO friendly |
| Academic papers | Title Case | Professional |
| JavaScript libraries | camelCase | Language convention |
| Configuration files | kebab-case | Readable, safe |
| Personal photos | kebab-case | Clean, readable |
| API endpoints | kebab-case | REST standard |
| Database tables | snake_case | SQL convention |
| Class files | PascalCase | OOP standard |
