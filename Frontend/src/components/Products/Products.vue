<template>
  <!-- 여기다 html -->
  <div class="products-content">
    <span>상품 관리</span>
    <div class="products-filter">
      <div class="search-date">
        <span class="date">조회 기간</span>
        <div class="input-date">
          <input class="start-date" placeholder="클릭해주세요.">
          <span class="range">~</span>
          <input class="end-date" placeholder="클릭해주세요.">
        </div> 
      </div>
    <div class="seller-name">
      <span>셀러명</span>
      <div class="search-select">
        <input type="text" placeholder="검색어를 입력하세요.">
        <select class="select">
          <option value>Select</option>
          <option value>상품명</option>
          <option value>상품번호</option>
          <option value>상품코드</option>
        </select>
        <input type="text" placeholder="검색어를 입력하세요.">
      </div>
    </div>
    <div class="seller-attribute">
      <span>셀러속성 :</span>
      <div class="attributes">
        <button class="all">전체</button>
        <button>쇼핑몰</button>
        <button>마켓</button>
        <button>로드샵</button>
        <button>디자이너브랜드</button>
        <button>제너럴브랜드</button>
        <button>내셔널브랜드</button>
        <button>뷰티</button>
      </div>
    </div>
    <div class="sell-info">
      <span>판매여부 :</span>
      <div class="sell-or-not">
        <button class="all">전체</button>
        <button>판매</button>
        <button>미판매</button>
      </div>
    </div>
    <div class="show-info">
      <span>진열여부 :</span>
      <div class="show-or-not">
        <button class="all">전체</button>
        <button>진열</button>
        <button>미진열</button>
      </div>
    </div>
    <div class="discount-info">
      <span>할인여부 :</span>
      <div class="discount-or-not">
        <button class="all">전체</button>
        <button>할인</button>
        <button>미할인</button>
      </div>
    </div>
    <div class="search-reset">
      <button class="search">검색</button>
      <button>초기화</button>
    </div>
  </div>
    <div class="page-bar"> 
    </div>
    <!-- <div class="sellers-content-header"> -->
    <div class="header-content">
      <div class="icon-span">
        <a-icon class="icon" type="unordered-list" />
        <span>상품관리 / 상품관리</span>
        <a-icon class="icon" type="right" />
        <span>상품관리 관리</span>
        <a-icon class="icon" type="right" />
        <span>리스트</span>
      </div>
      <div class="select-pagenation">
        <select>
          <option value>10개씩보기</option>
          <option value>20개씩보기</option>
          <option value>50개씩보기</option>
        </select>
      </div>
    </div>
  
    <!-- </div> -->
  <div class="product-excel">
        <button>
          <a-icon type="file-excel" />
          선택상품 엑셀다운로드
        </button>
        <button>
          <a-icon type="file-excel" />
          전체상품 엑셀다운로드
        </button>
        <select>
          <option value>판매여부</option>
          <option value>판매</option>
          <option value>미판매</option>
        </select>
        <select>
          <option value>진열여부</option>
          <option value>진열</option>
          <option value>미진열</option>
        </select>
        <button class="apply">
          <a-icon type="check" />
          적용
        </button>
      </div>

    <div class ="table">
      <span>전체 조회건 수 :  건</span>
    </div>
    <table>
      <thead>
        <tr>
          <th>
            <div>
              <a-checkbox
                :indeterminate="indeterminate"
                :checked="checkAll"
                @change="onCheckAllChange"
              />
            </div>
          </th>
          <th v-for="column in columns" :key="column.dataIndex">
            <div>
              {{ column.title }}
            </div>
          </th>
          <td>
            <div>
              <a-select
                :default-value="select_value"
                style="width: 80px"
                @change="searchSellerDropdown"
              >
                <a-select-option
                  v-for="stat in seller_status"
                  :key="stat.name"
                  name="seller_status"
                  :value="stat.seller_status_id"
                >
                  {{ stat.name }}
                </a-select-option>
              </a-select>
            </div>
          </td>
          <th scope="col">등록일</th>
          <th scope="col">대표이미지</th>
          <th scope="col">상품명</th>
          <th scope="col">상품코드</th>
          <th scope="col">상품번호</th>
          <th scope="col">셀러속성</th>
          <th scope="col">셀러명</th>
          <th scope="col">판매가</th>
          <th scope="col">할인가</th>
          <th scope="col">판매여부</th>
          <th scope="col">진열여부</th>
          <th scope="col">할인여부</th>
          <th scope="col">구매하기</th>
          <th scope="col" v-if="sheetStatus != 'WAIT'">응답상태</th>
          <th v-for="(question, index) in sheetQuestions" :key="index" scope="col">{{ question }}</th>
          <th scope="col" v-if="sheetStatus != 'WAIT'">응답날짜</th>
          <th scope="col" v-if="sheetStatus != 'WAIT'">수정날짜</th>
          <th scope="col" v-if="sheetStatus == 'PROCEEDING'">응답 수정</th>
          <th scope="col" v-if="sheetStatus == 'PROCEEDING'">메일 전송</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(line, index) in responseData" :key="index">
          <th scope="row">{{ index + 1 }}</th>
          <td>{{ line.name }}</td>
          <td>{{ line.position }}</td>
          <td>{{ line.teamName }}</td>
          <td v-if="sheetStatus != 'WAIT'">
            <span v-if="line.requestStatus == 'YES'" style=""><span class="dot dot-yes"></span></span>
            <span v-else>
              <div v-if="sheetStatus == 'PROCEEDING'" class="spinner-border spinner-border-sm text-danger" role="status">
                <span class="sr-only">Loading...</span>
              </div>
              <div v-else>
                <span class="dot dot-no"></span>
              </div>
            </span>
          </td>
          <td v-for="(text, index2) in line.response" :key="index2">{{ text }}</td>
          <td v-if="sheetStatus != 'WAIT'">{{ line.responseDate != null ? line.responseDate.split('T').join('  ') : '' }}</td>
          <td v-if="sheetStatus != 'WAIT'">{{ line.modifiedDate != null ? line.modifiedDate.split('T').join('  ') : '' }}</td>
          <td v-if="sheetStatus == 'PROCEEDING'"><Button class="btn btn-info">Edit</Button></td>
          <td v-if="sheetStatus == 'PROCEEDING'">
            <Button v-if="line.requestStatus == 'YES'" class="btn btn-warning">수정 요청</Button>
            <Button v-if="line.requestStatus == 'NO'" class="btn btn-warning">재전송</Button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "Products",

  data() {
    return {
      // state 관리
    };
  },

  methods: {
    // 함수
  },
};
</script>

<style lang="scss" scoped>
/* 여기다 스타일 */
.products-content {
    font-weight: lighter;
    font-size: 25px;
    padding: 20px 20px;
}

.products-filter {
    width:1132px;
    font-weight: 500;
    border: 3px #ccc solid;
    padding: 10px 25px 25px;
    margin: 10px 10px 20px 0px;
    font-size: 14px;
}

.search-date {
    position: relative;
}

.start-date {
    border-radius: 3px 0 0 3px;
    border-top-right-radius: 0;
    border-bottom-right-radius: 0;
    text-align: center;
    width: 30%;
    padding: 5px 10px;
}

.range {
    text-align: center;
    border-color: #ccc;
    background: #ccc;
    padding: 9px 17px 9px 17px;
    margin: auto -5px;
}

.end-date {
    border-radius: 0 3px 3px 0;
    text-align: center;
    width:30%;
    padding: 5px 10px;
}

button {
  border: 1px solid #ccc;
  background: white;
  padding: 5px 10px;
  border-radius: 3px;
}

input {
  border: 1px solid #ccc;
}

.input-date {
  display: inline-block;
  margin-left:50px;
}

.seller-name {
  margin-top: 5px;
}
.search-select {
  display: inline-block;
  margin-left:66px;
}

.select {
  margin-left: 50px;
  height: 32px;
  border: 1px solid #ccc; 
  border-radius: 3px;
  padding: 2px 10px;
}

.search-select input {
  width: 300px;
  height: 32px;
  border-radius: 3px;
  padding: 4px 10px;
  font-size: 14px;
}

.seller-attribute {
  margin-top: 10px;
}

.attributes {
  display: inline-block;
  margin-left:45px;
}

.sell-info {
  margin-top: 5px;
}

.sell-or-not {
  display: inline-block;
  margin-left:45px;
}

.show-info {
  margin-top: 5px;
}

.show-or-not {
  display: inline-block;
  margin-left:45px;
}

.discount-info {
  margin-top: 5px;
}

.discount-or-not {
  display: inline-block;
  margin-left:45px;
}

.search-reset {
  margin: 30px 40px 0px 38%;
}

.search-reset button {
  width: 20%;
  padding:6px 10px;
  text-align: center;
  border-radius: 0px;
}

button:hover {
  cursor: pointer;
  background-color: rgb(224, 223, 223);
  border-color: rgb(175, 174, 174);
}

.search {
  color: #fff;
  background-color: #428bca;
  border-color: #357ebd;
}

.search:hover {
  background-color: #2a6599;
  border-color: #214c72;
}

.all {
  color: #fff;
  background-color: #428bca;
  border-color: #357ebd;
}

.all:hover {
  background-color: #2a6599;
  border-color: #214c72;
}

.header-content {
  background-color: #e2e1e1;
  height:35px;
  margin-left: -20px;
  margin-right: -20px;
  padding-left: 10px;
  padding-right: 20px;
  display: flex;
}

.icon-span {
  width: 50%;
  height: 100%;
  display: inline;
  display: flex;
  align-items: center;
}

.icon-span span {
  font-size: 13px;
  font-weight: bold;
}

.icon {
  font-size: 13px;
  padding: 0 4px;

}

.select-pagenation {
  display: flex;
}

.select-pagenation select {
  position: absolute;
  right:90px;
  height: 30px;
  border: 1px solid #ccc;
  padding-bottom: 10px;
  border-radius: 3px;
  padding: 2px 10px;
  font-size: 13px;
  margin-top:2px;
}

.product-excel {
  position: absolute;
  right:58px;
}

.product-excel button {
  font-size: 12px;
  padding: 1px 5px;
  text-align: center;
  border-radius: 3px;
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}

button.apply {
  font-size: 13px;
  font-weight: bold;
  height: 30px;
  padding: 5px 10px;
  text-align: center;
  border-radius: 3px;
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}

.product-excel select {
  height: 30px;
  font-size:13px;
  padding: 2px 10px;
  font-weight: normal;
  color: #333333;
  background-color: white;
  border: 1px solid #e5e5e5;
  box-shadow: none;
  border-radius: 4px;
}

.table {
  margin-top:50px;
  font-size: 13px;
  font-weight: normal;
}

</style>