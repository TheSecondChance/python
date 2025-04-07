#!/bin/bash


RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' 

PROJECT_DIR=$(pwd)


EXTENSIONS="py html css js"


EXCLUDE_DIRS="venv|env|migrations|__pycache__|static|media|.git|node_modules"

echo -e "${GREEN}Counting lines of code in Django project at ${YELLOW}$PROJECT_DIR${NC}"
echo -e "${RED}Excluding: ${BLUE}$EXCLUDE_DIRS${NC}"
echo -e "${GREEN}--------------------------------------------${NC}"


declare -A EXTENSION_COUNTS
TOTAL_LOC=0
TOTAL_FILES=0


for ext in $EXTENSIONS; do
    echo -e "\n${YELLOW}${ext} files:${NC}"
    EXTENSION_COUNTS[$ext]=0
    FILE_COUNT=0
    
    while read file; do
       
        COUNT=$(wc -l < "$file")
        
       
        EXTENSION_COUNTS[$ext]=$((EXTENSION_COUNTS[$ext] + COUNT))
        TOTAL_LOC=$((TOTAL_LOC + COUNT))
        FILE_COUNT=$((FILE_COUNT + 1))
        TOTAL_FILES=$((TOTAL_FILES + 1))
        
        printf "  ${BLUE}%-6s${NC} %s\n" "$COUNT" "${file#$PROJECT_DIR/}"
    done < <(find "$PROJECT_DIR" -type f -name "*.$ext" | grep -Ev "$EXCLUDE_DIRS")

    echo -e "  ${GREEN}Total for .$ext: ${YELLOW}${EXTENSION_COUNTS[$ext]}${NC} lines in ${YELLOW}$FILE_COUNT${NC} files"

done


echo -e "\n${GREEN}--------------------------------------------"
echo -e "Summary:${NC}"
printf "${YELLOW}%-10s %12s %12s${NC}\n" "Extension" "Lines" "Files"
echo -e "${GREEN}--------------------------------------------${NC}"

for ext in $EXTENSIONS; do
    printf "%-10s %12s %12s\n" ".$ext" "${EXTENSION_COUNTS[$ext]}" "$(find "$PROJECT_DIR" -type f -name "*.$ext" | grep -Ev "$EXCLUDE_DIRS" | wc -l)"
done

echo -e "${GREEN}--------------------------------------------${NC}"
printf "${YELLOW}%-10s %12s %12s${NC}\n" "Total" "$TOTAL_LOC" "$TOTAL_FILES"
echo -e "${GREEN}--------------------------------------------${NC}"