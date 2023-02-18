const app = new Vue({
    el : '#app',
    data:{
        group_name : '',
        eklenenler: [
            {id:1, name:'abc'},
            {id:2, name:'mkj'},
            {id:3, name:'ygf'}
        ]
    },
    methods:{
        ekle(){
           const formData = new FormData();
           formData.append('groupname', this.group_name) ;
           axios.post('server.php?islem=addgroup', formData).then(res => console.log(res)).catch(err => console.log(err)) ;        
        }
    }
}) ;