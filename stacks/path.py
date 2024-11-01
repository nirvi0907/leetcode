class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []
        dirs = path.split('/')

        for dir_name in dirs:
            if not dir_name or dir_name=='.':
                continue
            if dir_name=='..':
                if stack:
                    stack.pop()
            else:
                stack.append(dir_name)

        return '/'+'/'.join(stack)