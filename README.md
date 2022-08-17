# IOT_hackathon

## S-DoT 데이터를 활용한 개인형 이동장치(PM)의 사고위험요인 분석 및 사고위험도 예측 🛴

### 📝 분석 방법
1. 선행연구 검토 후 유의미한 변수 및 추가로 고려대상이 될 변수 선정
2. 공간적 모델/시계열적 모델을 구분하여 PM 사고에 영향을 미치는 설명변수 탐색
   - Overdispersion/Zero Inflation Test
   - GLM 
   - Spatial Clustering with Spatial Autocorrelation Coefficients
   - Multivariate Time Series Analysis
3. 환경적 변수 및 지역적 변수에 기반한 예측 모델 생성
   - Multivariate LSTM-Fully Convolutional Network
   - Latent Feature Extraction with AutoEncoder
4. 22년 현재 데이터셋에 적용하여, 위험지역 발굴


### 📂 Repositories
- data : 분석에 필요한 각종 데이터 및 데이터셋 저장
- Seoul_Grid : 서울시 행정구역 그리드화
- TAAS : TAAS 교통사고데이터 크롤러
    *사고지점의 정확한 경도/위도 등 좌표를 제공하지 않으므로 동적 크롤러 이용하여 추출함
- StatsModel : 통계적 모델링을 위한 rep
- LSTM-FCN : LSTM-FCN network 모델을 위한 rep
- AutoEncoder : AutoEncoder 모델을 위한 rep

