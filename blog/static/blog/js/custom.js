function searchPost(){
    let searchValue = document.getElementById('search-input').value.trim();
    var selectValue = document.getElementById('ct').value;
    if(searchValue.length > 1){
        location.href="/search/" + selectValue + "/" + searchValue + "/";

    }
    else{
      alert('검색어('+ searchValue +')가 너무 짧습니다.');
    }
};
document.getElementById('search-input').addEventListener('keyup', function(event){
    if(event.key === 'Enter'){
      searchPost();
    }
});