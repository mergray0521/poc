// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TokenMinter {
    // Mapping to store token data
    mapping(uint256 => Token) public tokens;

    // Event emitted when a new token is minted
    event TokenMinted(uint256 tokenId, string tokenType, string materials, string color);

    // Struct to represent a token
    struct Token {
        string tokenType;
        string materials;
        string color;
        bool minted;
    }

    // Function to mint a new token
    function mintToken(
        uint256 tokenId,
        string memory tokenType,
        string memory materials,
        string memory color
    ) public {
        // Ensure the token ID is unique
        require(!tokens[tokenId].minted, "Token ID already minted");

        // Create a new token
        Token memory newToken = Token({
            tokenType: tokenType,
            materials: materials,
            color: color,
            minted: true
        });

        // Store the new token
        tokens[tokenId] = newToken;

        // Emit the TokenMinted event
        emit TokenMinted(tokenId, tokenType, materials, color);
    }

    // Function to get token details
    function getTokenDetails(uint256 tokenId) public view returns (Token memory) {
        return tokens[tokenId];
    }
}
