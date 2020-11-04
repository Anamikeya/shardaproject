function findTotal(){
    var arr = document.getElementsByClassName('eval-marks');
    var tot=0;
    for(var i=0;i<arr.length;i++){
        if(parseInt(arr[i].value))
            tot += parseInt(arr[i].value);
    }
    document.getElementById('total').value = tot;
    console.log(arr);
}

var guideEmail = {
  TestMail: ["test@gmail.com"],
  "Prof. (Dr.) Parma Nand": ["parma.nand@sharda.ac.in"],
  "Prof. (Dr.) Nitin Rakesh": ["nitin.rakesh@sharda.ac.in"],
  "Prof. (Dr.) Shri Kant": ["shri.kant@sharda.ac.in"],
  "Prof. (Dr.) Anil Kumar Sagar": ["Prof. (Dr.) Anil Kumar Sagar"],
  "Prof. (Dr.) Arun Prakash Agarwal": ["Prof. (Dr.) Arun Prakash Agarwal"],
  "Prof. (Dr.) Ankur Choudhary": ["ankur.choudhary@sharda.ac.in"],
  "Prof. (Dr.) Rukaiya Khanam": ["ruqaiya.khanam@sharda.ac.in"],
  "Dr. Mandeep Kaur": ["mandeep.kaur@sharda.ac.in"],
  "Dr. Gaurav Raj": ["gaurav.raj@sharda.ac.in"],
  "Dr. Mohit Agarwal": ["mohit.agarwal1@sharda.ac.in "],
  "Dr. Sudeshna Chakraborty": ["sudeshna.chakraborty@sharda.ac.in"],
  "Dr. Ali Imam Abidi": ["ali.abidi@sharda.ac.in"],
  "Dr. Vijendra Singh": ["vijendra.singh1@sharda.ac.in"],
  "Dr. Amrita": ["amrita.prasad@sharda.ac.in"],
  "Dr. Mayank Kumar Goyal": ["mayank.goyal2@sharda.ac.in"],
  "Dr. Latha Banda": ["latha.banda@sharda.ac.in"],
  "Dr. Hoor Fatima": ["hoor.fatima@sharda.ac.in"],
  "Dr. Nitish Kumar": ["nitish.kumar7@sharda.ac.in"],
  "Mr. Sudeep Varshney": ["sudeep.varshney@sharda.ac.in"],
  "Mr. Pradeep Kumar Mishra": ["pradeepkumar.mishra@sharda.ac.in"],
  "Mr. Gouri Shankar Mishra": ["gourisankar.mishra@sharda.ac.in"],
  "Mr. Amit Upadhyay": ["amitkumar.upadhyay@sharda.ac.in"],
  "Ms. Preeti Kaushik": ["preeti.kaushik@sharda.ac.in"],
  "Ms. Shaveta Khepra": ["shaveta.khepra@sharda.ac.in"],
  "Ms. Jyotsna Seth": ["jyotsna.seth@sharda.ac.in"],
  "Ms. Anamika Mitra": ["anamika.mitra@sharda.ac.in"],
  "Mr. Devendra Gautam": ["devendra.gautam@sharda.ac.in"],
  "Ms. Rani Astya": ["rani.astya@sharda.ac.in"],
  "Mr. Manish Verma": ["manish.verma1@sharda.ac.in"],
  "Mr. Dharm Raj": ["dharm.raj@sharda.ac.in"],
  "Mr. Pankaj Sharma": ["pankaj.sharma1@sharda.ac.in"],
  "Mr. Tarun Maini": ["tarun.maini@sharda.ac.in"],
  "Ms. Preeti Dubey": ["preeti.dubey@sharda.ac.in"],
  "Mr. Sunil Kumar": ["sunil.kumar7@sharda.ac.in"],
  "Ms. Kanika Singla": ["kanika.singla@sharda.ac.in"],
  "Ms. Megha Chhabra": ["megha.chhabra@sharda.ac.in"],
  "Ms. Abha Kiran Rajpoot": ["abhakiran.rajpoot@sharda.ac.in"],
  "Ms. Deepti Sahu": ["deepti.sahu@sharda.ac.in"],
  "Mr. Subrata Sahana": ["subrata.sahana@sharda.ac.in"],
  "Ms. Pragya Mishra": ["pragya.mishra@sharda.ac.in"],
  "Mr. Abhishek Singh Verma": ["abhishek.verma1@sharda.ac.in"],
  "Ms. Ritu Dewan": ["ritu.dewan@sharda.ac.in"],
  "Ms. Neha Tyagi": ["neha.tyagi1@sharda.ac.in"],
  "Mr. Sushant Jhingran": ["sushant.jhingran@sharda.ac.in"],
  "Ms. Gunjan Agarwal": ["gunjan.aggarwal@sharda.ac.in"],
  "Mr. Satendra Kumar": ["satendra.kumar@sharda.ac.in"],
  "Mr. Jagdeep Singh": ["jagdeep.singh@sharda.ac.in"],
  "Mr. Tejaswi Khanna": ["tejaswi.khanna@sharda.ac.in"],
  "Mr. Bharat Bhushan": ["bharat.bhushan@sharda.ac.in"],
  "Mr. Avinash Kumar": ["avinash.kumar5@sharda.ac.in"],
}

var main = document.getElementById("main_menu")
var sub = document.getElementById("sub_menu")

main.addEventListener("change", function () {
  var selected_option = guideEmail[this.value]
  while (sub.options.length > 0) {
    sub.options.remove(0)
  }
  Array.from(selected_option).forEach(function (e1) {
    let option = new Option(e1, e1)
    sub.appendChild(option)
    console.log(option)
  })
})
