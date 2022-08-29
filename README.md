# IOT_hackathon

## S-DoT 데이터를 활용한 개인형 이동장치(PM)의 사고위험요인 분석 및 사고위험도 예측 🛴

### 📝 분석 방법
1. 선행연구 검토 후 유의미한 변수 및 추가로 고려대상이 될 변수 선정
2. 기존 분석계획 : 각 격자별 시계열 데이터 생성으로 공간적 분석 및 시계열적 분석 모두 진행
- 환경적 변수 및 지역적 변수 발굴하여
- Multivariate LSTM-FCN 등을 이용한 위험지역 예측 모델 생성
  
> 데이터셋이 과도하게 커져 제한시간(해커톤) 내 문제해결하지 못할 가능성 파악하여
> 사고데이터를 중심으로 사고의 심각도(순서형 변수)를 종속변수로 한 심각도 분석 모형 개발
> **Ordinal Probit Regression** 이용하였으며, `statsmodels` 패키지 이용함(구체적인 모형은 코드 참고)


### 📂 Repositories
- Preprocessing : 분석에 필요한 각종 데이터 및 데이터셋, 전처리과정 저장(원본데이터셋 저장 X)
- Seoul_Grid : 서울시 행정구역 그리드화
- TAAS : TAAS 교통사고데이터 크롤러
> 사고지점의 정확한 경도/위도 등 좌표를 제공하지 않으므로 `selenium`을 이용한 동적 크롤러를 개발하여 각 사고지점의 좌표를 추출함
- 최종 데이터셋 : `Dataset.csv` 및 생성과정 at `SDoT 데이터 병합.ipynb`
- 분석모형 : `OrdinalRegression.ipynb`
- LSTM-FCN : LSTM-FCN network 모델을 위한 rep(모델 생성 but 주제 변경으로 이용은 하지 못함)

### 👮‍♂️ Collaborators
- [@ddangchani](https://github.com/ddangchani) [@birdkang](https://github.com/birdkang) [@cheygoon](https://github.com/cheygoon) [@thiefmouse96](https://github.com/thiefmouse96)
