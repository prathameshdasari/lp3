// SPDX-License-Identifier: MIT
pragma solidity  ^0.8.0;

contract banking{
  mapping(address=>uint) public userAccount;
  mapping(address=>bool) public userExists;

  function createAcc() public payable returns(string memory){
      require(userExists[msg.sender]==false,'Account Already Created');
      if(msg.value==0){
          userAccount[msg.sender]=0;
          userExists[msg.sender]=true;
          return 'account created';
      }
      require(userExists[msg.sender]==false,'account already created');
      userAccount[msg.sender] = msg.value;
      userExists[msg.sender] = true;
      return 'account created';
  }
  
  function deposit() public payable returns(string memory){
      require(userExists[msg.sender]==true, 'Account is not created');
      require(msg.value>0, 'Value for deposit is Zero');
      userAccount[msg.sender]=userAccount[msg.sender]+msg.value;
      return 'Deposited Succesfully';
  }
  
  function withdraw(uint amount) public payable returns(string memory){
      require(userAccount[msg.sender]>amount, 'insufficeint balance in Bank account');
      require(userExists[msg.sender]==true, 'Account is not created');
      require(amount>0, 'Enter non-zero value for withdrawal');
      userAccount[msg.sender]=userAccount[msg.sender]-amount;
      payable(msg.sender).transfer(amount);
      return 'withdrawal Succesful';
  }
 
  function userAccountBalance() public view returns(uint){
      return userAccount[msg.sender];
  }
   
}