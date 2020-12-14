<template>
  <!-- 여기다 html -->
  <div class="products-content">
    <span>상품 관리</span>
    <div class="products-filter">
      <div class="search-date">
        <span class="date">조회 기간</span>
        <div class="input-date">
          <a-date-picker class="start-date" @change="getStartDate" data-id="start_date" placeholder="클릭해주세요." />
          <span class="range">~</span>
          <a-date-picker class="end-date" @change="getEndDate" data-id="end_date" placeholder="클릭해주세요." />
        </div> 
      </div>
    <div class="seller-name">
      <span>셀러명</span>
      <div class="search-select">
        <input type="text" placeholder="검색어를 입력하세요." data-id="seller_name" @blur="searchInputData">
        <select class="select" @change="onChange($event)">
          <option value>Select</option>
          <option v-for="search in select_search" data-id=search.id :key="search.id">{{ search.name }}</option>
        </select>
        <input type="text" placeholder="검색어를 입력하세요.">
      </div>
    </div>
    <div class="seller-attribute">
      <span>셀러속성 :</span>
      <div class="attributes">
        <button class="all">전체</button>
        <button v-for="attribute in attributes" @click="searchInputData" data-id="seller_attribute_id"  :value="attribute.id" :key="attribute.id">{{ attribute.name }}</button>
      </div>
    </div>
    <div class="sell-info">
      <span>판매여부 :</span>
      <div class="sell-or-not">
        <button class="all">전체</button>
        <button v-for="info in sell_info" @click="searchInputData" data-id="sell_info" :value="info.id" :key="info.id">{{ info.name }}</button>
      </div>
    </div>
    <div class="show-info">
      <span>진열여부 :</span>
      <div class="show-or-not">
        <button class="all">전체</button>
        <button v-for="info in show_info" @click="searchInputData" data-id="show_info" :value="info.id" :key="info.id">{{ info.name }}</button>
      </div>
    </div>
    <div class="discount-info">
      <span>할인여부 :</span>
      <div class="discount-or-not">
        <button class="all">전체</button>
        <button v-for="info in sale_info" @click="searchInputData" data-id="sale_info" :value="info.id" :key="info.id">{{ info.name }}</button>
      </div>
    </div>
    <div class="search-reset">
      <button class="search" @click.prevent="submitData">검색</button>
      <input type='reset' @click="resetData">
    </div>
  </div>
    <div class="page-bar"> 
    </div>
    <div class="header-content">
      <div class="icon-span">
        <a-icon class="icon" type="unordered-list" />
        <span>상품관리 / 상품관리</span>
        <a-icon class="icon" type="right" />
        <span>상품관리 관리</span>
        <a-icon class="icon" type="right" />
        <span>리스트</span>
      </div>
      <div class="select-pagination">
        <select>
          <option v-for="pagination in select_pagination" data-id="limit" :value="pagination.id" :key="pagination.id">{{ pagination.name }}</option>
        </select>
      </div>
    </div>
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
          <option v-for="info in sell_info" @click="sellInfo" :key="info.id">{{ info.name }}</option>
        </select>
        <select>
          <option value>진열여부</option>
          <option v-for="info in show_info" @click="showInfo" :id="info.id" :key="info.id">{{ info.name }}</option>
        </select>
        <button class="apply">
          <a-icon type="check" />
          적용
        </button>
      </div>

    <div class ="table">
      <span>전체 조회건 수 : {{count}}건</span>
    </div>
    <div>
      <table id="product-list">
        <thead>
          <tr class="heading">
            <th width="110">등록일</th>
            <th width ="100">대표이미지</th>
            <th width="100">상품명</th>
            <th width="70">상품코드</th>
            <th width="70">상품번호</th>
            <th width="70">셀러속성</th>
            <th width="80">셀러명</th>
            <th width="70">판매가</th>
            <th width="70">할인가</th>
            <th width="70">판매여부</th>
            <th width="70">진열여부</th>
            <th width="70">할인여부</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="row in rows">
            <td>{{row.created_at}}</td>
            <td class="table-img">
              <img :src="row.thumbnail" alt="">
            </td>
            <td>{{row.name}}</td>
            <td>{{row.code}}</td>
            <td>{{row.number}}</td>
            <td>{{row.seller_attribute}}</td>
            <td>{{row.seller_name}}</td>
            <td>{{row.price}}</td>
            <td>{{row.price}}</td>
            <td v-if="row.sell_info===1">판매</td>
            <td v-if="row.sell_info===0">미판매</td>
            <!-- <td>{{row.show_info}}</td> -->
            <td v-if="row.show_info===1">진열</td>
            <td v-if="row.show_info===0">미진열</td>
            <!-- <td>{{row.sale_info}}</td> -->
            <td v-if="row.sale_info===1">할인</td>
            <td v-if="row.sale_info===0">미할인</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { mapState} from "vuex"

export default {
  name: "Products",
  

  data() {
    return {
      sell_info: [
        { id: 1, name: '판매'},
        { id: 0, name: '미판매'}
      ],
      show_info: [
        { id: 1, name: '진열'},
        { id: 0, name: '미진열'}
      ],
      sale_info: [
        { id: 1, name: '할인'},
        { id: 0, name: '미할인'}
      ],
      select_search: [
        { id: "product_name", name: "상품명"},
        { id: "product_number", name: "상품번호"},
        { id: "product_code", name: "상품코드"}
      ],
      attributes: [
        { id: 1, name: '쇼핑몰' },
        { id: 2, name: '마켓' },
        { id: 3, name: '로드샵' },
        { id: 4, name: '디자이너브랜드' },
        { id: 5, name: '제너럴브랜드' },
        { id: 6, name: '내셔널브랜드' },
        { id: 7, name:  '뷰티' }
      ],
      select_pagination: [
        { id: 10, name: "10개씩보기"},
        { id: 20, name: "20개씩보기"},
        { id: 50, name: "50개씩보기"}
      ],
      rows: [],
      count: "",
      searchInput: {
        start_date: null,
        end_date:null,
        seller_attribute_id: 0,
        sell_info:0,
        show_info:0,
        sale_info:0
      },
      resetData: {
        start_date: null,
        end_date:null,
        seller_attribute_id: 0,
        seller_name:"",
        sell_info:0,
        show_info:0,
        sale_info:0
      }
    };
  },

  computed:{
    ...mapState({
      user_token: ({ users }) => users.user_token,
    })
  },

  methods: {

    searchInputData(e) {
      const {id} = e.target.dataset
      const {value} = e.target
      this.searchInput={
        ...this.searchInput,
        [id]: value
      }

      console.log(this.searchInput)
    },

    getStartDate( date, dateString) {
      this.searchInput.start_date = dateString
    },

    getEndDate( date, dateString) {
      this.searchInput.end_date = dateString
      console.log(this.searchInput)
    },

    onChange(event) {
      console.log(event.target.value);
    },

    showInfo(e){
      console.log(e.target.dataset.id)
    },

    sellInfo(e){
      console.log(e.target.dataset.id)
    },

    async submitData(){
      const headers = {
        headers :{
          Authorization: this.user_token
        }
      }

      console.log()
      let query = "http://localhost:5000/master/product_list?offset=0&limit=40"
      Object.keys(this.searchInput).forEach(el => {
        query += `&${el}=${this.searchInput[el]}`
      } )
      const response = await this.$http.get(query, headers)
      const {product_count, product_list} = response.data
      this.rows = product_list
      this.count = product_count.product_count
      console.log(this.rows, "!@#!#!@#!!#!@#!3")
    },
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
    width: 100%;
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
    width: 40%;
}

.range {
    text-align: center;
    font-size: 18px;
    // border-color: #ccc;
    // background: #ccc;
    padding: 7px 17px 7px 17px;
    margin: auto -5px;
}

.end-date {
    border-radius: 0 3px 3px 0;
    text-align: center;
    width:40%;
}

button {
  border: 1px solid #ccc;
  background: white;
  padding: 5px 10px;
  margin: 0 1px;
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

.search-reset input {
  width: 20%;
  padding:6px 10px;
  text-align: center;
  border-radius: 0px;
  background: white;
}

.search-reset input:hover {
  cursor: pointer;
  background-color: rgb(224, 223, 223);
  border-color: rgb(175, 174, 174);
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
  width: 120%;
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

.select-pagination {
  display: flex;
}

.select-pagination select {
  position: relative;
  left:285%;
  height: 30px;
  border: 1px solid #ccc;
  padding-bottom: 10px;
  border-radius: 3px;
  padding: 2px 10px;
  font-size: 13px;
  margin-top:2.4px;
}

.product-excel {
  position: relative;
  left:43%;
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

table {
  width: 100%;
  border-collapse: collapse;
  border: 1px solid #ccc;
  font-size: 14px;
  font-weight: 600;
  background-color: white;
  overflow-x: auto;
  overflow-y: hidden;
}

.table{
  font-weight: bold;
  margin-bottom: 5px;
}

table th {
  text-align: left;
  color: black;
  padding: 8px;
  font-size: 13px;
  border: 1px solid #ccc;
  background-color: #e2e1e1;
}

table td {
  text-align: left;
  color: black;
  padding: 8px;
  border: 1px solid #ccc;
  font-size: 13px;
  font-weight: lighter;
}

.checkbox {
  padding-right:2px;
  padding-left: 11px;
  border: 1px solid #ccc;
}

button:focus {
  color: #fff;
  background-color: #428bca;
  border-color: #357ebd;
}

.table-img {
  width: 120px;

  >img {
    width: 100%;
    height: auto;
  }
}
</style>