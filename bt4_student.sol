// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    struct Student {
        uint id;
        string name;
        uint age;
    }

    Student[] public students;
    address public owner;

    constructor() 
    {
        owner = msg.sender;
    }

    function addStudent(uint _id, string memory _name, uint _age) public 
    {
        students.push(Student(_id, _name, _age));
    }

    // Function to retrieve a student's details by index
    function getStudent(uint index) public view returns (uint, string memory, uint) 
    {
        require(index < students.length, "Invalid index");
        Student memory student = students[index];
        return (student.id, student.name, student.age);
    }

    // Receive function to accept incoming Ether with no data
    receive() external payable {
        // Optionally log an event or take other action if needed
    }

    // Fallback function to handle calls with data that do not match any function signature
    fallback() external payable {
        // Optionally log an event or take other action if needed
    }

    // Function to get the number of students in the array
    function getStudentCount() public view returns (uint) 
    {
        return students.length;
    }
}
